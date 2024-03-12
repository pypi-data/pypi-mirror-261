# Copyright (c) Chris G. Van de Walle
# Distributed under the terms of the MIT License.

"""Convenience utilities for nonrad.

This module contains various convenience utilities for working with and
preparing input for nonrad.
"""

from typing import Union

import numpy as np
from pymatgen.core import Structure
from pymatgen.io.vasp.outputs import Vasprun
from scipy.optimize import curve_fit

from nonrad.constants import AMU2KG, ANGS2M, EV2J, HBAR


def get_cc_structures(
        ground: Structure,
        excited: Structure,
        displacements: np.ndarray,
        remove_zero: bool = True
) -> tuple[list, list]:
    """Generate the structures for a CC diagram.

    Parameters
    ----------
    ground : pymatgen.core.structure.Structure
        pymatgen structure corresponding to the ground (final) state
    excited : pymatgen.core.structure.Structure
        pymatgen structure corresponding to the excited (initial) state
    displacements : list(float)
        list of displacements to compute the perturbed structures. Note: the
        displacements are for only one potential energy surface and will be
        applied to both (e.g. displacements=np.linspace(-0.1, 0.1, 5)) will
        return 10 structures 5 of the ground state displaced at +-10%, +-5%,
        and 0% and 5 of the excited state displaced similarly)
    remove_zero : bool
        remove 0% displacement from list (default is True)

    Returns
    -------
    ground_structs = list(pymatgen.core.structure.Struture)
        a list of structures corresponding to the displaced ground state
    excited_structs = list(pymatgen.core.structure.Structure)
        a list of structures corresponding to the displaced excited state
    """
    displacements = np.array(displacements)
    if remove_zero:
        displacements = displacements[displacements != 0.]
    ground_structs = ground.interpolate(excited, nimages=displacements)
    excited_structs = ground.interpolate(excited, nimages=(displacements + 1.))
    return ground_structs, excited_structs


def get_dQ(ground: Structure, excited: Structure) -> float:
    """Calculate dQ from the initial and final structures.

    Parameters
    ----------
    ground : pymatgen.core.structure.Structure
        pymatgen structure corresponding to the ground (final) state
    excited : pymatgen.core.structure.Structure
        pymatgen structure corresponding to the excited (initial) state

    Returns
    -------
    float
        the dQ value (amu^{1/2} Angstrom)
    """
    return np.sqrt(np.sum(list(map(
        lambda x: x[0].distance(x[1])**2 * x[0].specie.atomic_mass,
        zip(ground, excited)
    ))))


def get_Q_from_struct(
        ground: Structure,
        excited: Structure,
        struct: Union[Structure, str],
        tol: float = 1e-4,
        nround: int = 5,
) -> float:
    """Calculate the Q value for a given structure.

    This function calculates the Q value for a given structure, knowing the
    endpoints and assuming linear interpolation.

    Parameters
    ----------
    ground : pymatgen.core.structure.Structure
        pymatgen structure corresponding to the ground (final) state
    excited : pymatgen.core.structure.Structure
        pymatgen structure corresponding to the excited (initial) state
    struct : pymatgen.core.structure.Structure or str
        pymatgen structure corresponding to the structure we want to calculate
        the Q value for (may also be a path to a file containing a structure)
    tol : float
        distance cutoff to throw away coordinates for determining Q (sites that
        don't move very far could introduce numerical noise)
    nround : int
        number of decimal places to round to in determining Q value

    Returns
    -------
    float
        the Q value (amu^{1/2} Angstrom) of the structure
    """
    if isinstance(struct, str):
        tstruct = Structure.from_file(struct)
    else:
        tstruct = struct

    dQ = get_dQ(ground, excited)

    excited_coords = excited.cart_coords
    ground_coords = ground.cart_coords
    struct_coords = tstruct.cart_coords

    dx = excited_coords - ground_coords
    ind = np.abs(dx) > tol

    poss_x = np.round((struct_coords - ground_coords)[ind] / dx[ind], nround)
    val, count = np.unique(poss_x, return_counts=True)

    return dQ * val[np.argmax(count)]


def get_PES_from_vaspruns(
        ground: Structure,
        excited: Structure,
        vasprun_paths: list[str],
        tol: float = 0.001
) -> tuple[np.ndarray, np.ndarray]:
    """Extract the potential energy surface (PES) from vasprun.xml files.

    This function reads in vasprun.xml files to extract the energy and Q value
    of each calculation and then returns it as a list.

    Parameters
    ----------
    ground : pymatgen.core.structure.Structure
        pymatgen structure corresponding to the ground (final) state
    excited : pymatgen.core.structure.Structure
        pymatgen structure corresponding to the excited (initial) state
    vasprun_paths : list(strings)
        a list of paths to each of the vasprun.xml files that make up the PES.
        Note that the minimum (0% displacement) should be included in the list,
        and each path should end in 'vasprun.xml' (e.g. /path/to/vasprun.xml)
    tol : float
        tolerance to pass to get_Q_from_struct

    Returns
    -------
    Q : np.array(float)
        array of Q values (amu^{1/2} Angstrom) corresponding to each vasprun
    energy : np.array(float)
        array of energies (eV) corresponding to each vasprun
    """
    num = len(vasprun_paths)
    Q, energy = (np.zeros(num), np.zeros(num))
    for i, vr_fname in enumerate(vasprun_paths):
        vr = Vasprun(vr_fname, parse_dos=False, parse_eigen=False)
        Q[i] = get_Q_from_struct(ground, excited, vr.structures[-1], tol=tol)
        energy[i] = vr.final_energy
    return Q, (energy - np.min(energy))


def get_omega_from_PES(
        Q: np.ndarray,
        energy: np.ndarray,
        Q0: Union[float, None] = None,
        ax=None,
        q: Union[np.ndarray, None] = None
) -> float:
    """Calculate the harmonic phonon frequency for the given PES.

    Parameters
    ----------
    Q : np.array(float)
        array of Q values (amu^{1/2} Angstrom) corresponding to each vasprun
    energy : np.array(float)
        array of energies (eV) corresponding to each vasprun
    Q0 : float
        fix the minimum of the parabola (default is None)
    ax : matplotlib.axes.Axes
        optional axis object to plot the resulting fit (default is None)
    q : np.array(float)
        array of Q values to evaluate the fitting function at

    Returns
    -------
    float
        harmonic phonon frequency from the PES in eV
    """
    def f(Q, omega, Q0, dE):
        return 0.5 * omega**2 * (Q - Q0)**2 + dE

    # set bounds to restrict Q0 to the given Q0 value
    bounds = (-np.inf, np.inf) if Q0 is None else \
        ([-np.inf, Q0 - 1e-10, -np.inf], [np.inf, Q0, np.inf])
    popt, _ = curve_fit(f, Q, energy, bounds=bounds)    # pylint: disable=W0632

    # optional plotting to check fit
    if ax is not None:
        q_L = np.max(Q) - np.min(Q)
        if q is None:
            q = np.linspace(np.min(Q) - 0.1 * q_L, np.max(Q) + 0.1 * q_L, 1000)
        ax.plot(q, f(q, *popt))

    return HBAR * popt[0] * np.sqrt(EV2J / (ANGS2M**2 * AMU2KG))


def get_barrier_harmonic(
        dQ: float,
        dE: float,
        wi: float,
        wf: float
) -> Union[float, None]:
    """Calculate the barrier height within the Harmonic approximation.

    Parameters
    ----------
    dQ : float
        displacement between harmonic oscillators in amu^{1/2} Angstrom
    dE : float
        energy offset between the two harmonic oscillators
    wi, wf : float
        frequencies of the harmonic oscillators in eV

    Returns
    -------
    float, None
        barrier energy in eV or None if no crossing found
    """
    swi = wi / HBAR / np.sqrt(EV2J / (ANGS2M**2 * AMU2KG))
    swf = wf / HBAR / np.sqrt(EV2J / (ANGS2M**2 * AMU2KG))
    r = np.roots([
        0.5 * (swi**2 - swf**2),
        -swi**2 * dQ,
        dE + 0.5 * swi**2 * dQ**2,
    ])

    # no crossing point was found
    if not np.any(np.isreal(r)):
        return None

    return np.min(0.5 * swf**2 * r[np.isreal(r)]**2) - dE
