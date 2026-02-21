import numpy as np
import matplotlib.pyplot as plt

# PPT-Atoms Validation Suite v1.0.0 & PPT-Bio
# Script: DNA_Hydrogen_Bond_Geometric_Drift.py
# Author: Vladimir Milosevic
# Theory: Plasma Pressure Theory (PPT) 3.0
# Description: Models carcinogenesis as hydrostatic misalignment and geometric drift of DNA hydrogen bonds.

def simulate_dna_geometric_drift():
    print("--- PPT - Atoms: PPT 3.0: DNA Hydrogen Bond Hydrostatic Drift Solver ---")

    # 1. PPT 3.0 EXACT CONSTANTS
    c = 299792458  # Exact wave speed of the universal medium (m/s)
    P_univ = 2.06e34 # Universal hydrostatic background pressure (Pa or J/m^3)
    eV_to_Joules = 1.60218e-19

    # 2. THE HEALTHY BASELINE (Guanine-Cytosine H-Bond)
    # Standard average energy of a strong DNA H-bond is ~0.15 eV
    E_bond_eV = 0.15 
    E_bond_J = E_bond_eV * eV_to_Joules

    # Calculate the exact Geometric Overlap Void (Delta V) that creates this lock
    # Formula: dV = E / P_univ
    dV_healthy = E_bond_J / P_univ
    print(f"1. Universal Pressure (P_univ): {P_univ:.2e} Pa")
    print(f"2. Healthy G-C Bond Overlap Void: {dV_healthy:.4e} m^3\n")

    # 3. SIMULATING CANCER (HYDROSTATIC GEOMETRIC DRIFT)
    # 0% drift = Perfect Health. 100% drift = Bond completely fractures.
    drift_percentage = np.linspace(0, 100, 200)

    # As the bond drifts due to trauma (radiation/acoustic fatigue), 
    # the geometric overlap decreases, weakening the pinning pressure.
    overlap_retention = 1 - (drift_percentage / 100)**2 
    current_bond_energy_eV = E_bond_eV * overlap_retention

    # The "Structural Tension" is the difference between ideal hydrostatic pressure and actual pressure
    structural_tension = E_bond_eV - current_bond_energy_eV

    # --- HIGH-VISIBILITY VISUAL PROOF ---
    fig, ax1 = plt.subplots(figsize=(11, 6.5))
    
    # Plot 1: Remaining Pinning Pressure (Cyan)
    color1 = '#00FFFF'
    ax1.set_xlabel('Geometric Drift / Misalignment (%)', fontsize=12)
    ax1.set_ylabel('Remaining Hydrostatic Pinning Pressure (eV)', color=color1, fontsize=12)
    ax1.plot(drift_percentage, current_bond_energy_eV, color=color1, linewidth=3, label='Bond Strength (Pinning Pressure)', zorder=4)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, linestyle='--', alpha=0.3)

    # Highlight the "Cancer Zone" (Carcinogenesis)
    ax1.axvspan(30, 60, color='#e63946', alpha=0.2, label='Carcinogenesis Risk Zone')
    ax1.axvline(x=30, color='#FFD700', linestyle='--', linewidth=2, label='Mutation Threshold (30% Drift)', zorder=5)
    
    bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.9)
    ax1.text(32, 0.05, 'Carcinogenesis\n(Structure Bends but Survives)', color='black', bbox=bbox_props, fontweight='bold', fontsize=10)

    # Second Y-axis for Structural Tension (Gold/Red)
    ax2 = ax1.twinx()  
    color2 = '#FFD700' # High-vis Gold
    ax2.set_ylabel('Lattice Tension / Instability (eV)', color=color2, fontsize=12)  
    ax2.plot(drift_percentage, structural_tension, color=color2, linewidth=3, linestyle=':', label='Structural Tension', zorder=3)
    ax2.tick_params(axis='y', labelcolor=color2)

    # Styling
    plt.title('PPT-Bio: DNA Structural Failure and the Carcinogenesis Threshold', fontsize=14, pad=20)
    
    # Combine legends from both axes
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper center', frameon=True, facecolor='white', framealpha=0.9)
    
    fig.tight_layout()  
    plt.show()

if __name__ == "__main__":
    simulate_dna_geometric_drift()