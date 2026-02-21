import numpy as np
import matplotlib.pyplot as plt

# PPT-Atoms Validation Suite v1.0.0 & PPT-Bio
# Script: Resonance_Cure_Targeting_Solver.py
# Author: Vladimir Milosevic
# Theory: Plasma Pressure Theory (PPT) 3.0
# Description: Calculates the exact Terahertz resonance required to restore hydrostatic pinning pressure to a drifting DNA bond.

def calculate_resonance_restoration():
    print("--- PPT - Atoms: PPT 3.0: Targeted Geometric Restoration (The Resonance Cure) ---")

    # 1. PPT 3.0 CONSTANTS
    E_healthy_bond_eV = 0.15  # Baseline hydrostatic pinning pressure of a G-C bond
    
    # Planck's constant reframed as the Medium's Viscoelastic Harmonic Constant
    h_eV_s = 4.135667696e-15  

    # 2. DIAGNOSTIC SIMULATION
    # Testing a Healthy cell, a Carcinogenic cell (45% drift), and a Necrotic cell (90% drift)
    drifts = np.array([0, 45, 90])  

    print("\nCell Diagnostics & Acoustic Targeting:")
    print("-" * 85)
    print(f"{'Status':<22} | {'Drift (%)':<10} | {'Deficit (eV)':<15} | {'Restoration Wave (THz)'}")
    print("-" * 85)

    for drift in drifts:
        # Calculate remaining pinning pressure
        overlap_retention = 1 - (drift / 100)**2
        current_pressure_eV = E_healthy_bond_eV * overlap_retention
        
        # Calculate the HYDROSTATIC DEFICIT
        pressure_deficit_eV = E_healthy_bond_eV - current_pressure_eV
        
        # 3. THE RESTORATION WAVE (f = E_deficit / h)
        if drift < 80:
            restoration_frequency_Hz = pressure_deficit_eV / h_eV_s
            restoration_frequency_THz = restoration_frequency_Hz / 1e12 
            status = "HEALTHY" if drift == 0 else "CARCINOGENIC (DRIFT)"
            freq_str = f"{restoration_frequency_THz:.3f} THz"
        else:
            status = "NECROTIC (SHATTERED)"
            freq_str = "N/A (Lattice Destroyed)"
            
        print(f"{status:<22} | {drift:<10} | {pressure_deficit_eV:<15.4f} | {freq_str}")

    print("-" * 85)
    print("Mechanical Conclusion:")
    print("By treating Planck's constant as a viscoelastic resistance factor, targeted")
    print("Terahertz waves can theoretically restore the geometric tension of failing DNA.")

    # --- HIGH-VISIBILITY VISUAL PROOF ---
    drift_range = np.linspace(0, 80, 200)
    deficits = E_healthy_bond_eV - (E_healthy_bond_eV * (1 - (drift_range / 100)**2))
    frequencies_THz = (deficits / h_eV_s) / 1e12

    plt.figure(figsize=(11, 6.5))

    # The required restoration frequency curve (Cyan)
    plt.plot(drift_range, frequencies_THz, color='#00FFFF', linewidth=3, label='Required Harmonic Restoration Frequency', zorder=3)
    plt.fill_between(drift_range, frequencies_THz, color='#00FFFF', alpha=0.1)

    # Highlight a specific theoretical tumor targeting (Magenta)
    tumor_drift = 45
    tumor_deficit = E_healthy_bond_eV - (E_healthy_bond_eV * (1 - (tumor_drift / 100)**2))
    tumor_freq = (tumor_deficit / h_eV_s) / 1e12

    plt.scatter([tumor_drift], [tumor_freq], color='#FF00FF', s=150, zorder=5, 
                edgecolors='white', linewidths=2, label=f'Target Tumor (45% Drift)\nRequired Cure: {tumor_freq:.2f} THz')
    
    plt.vlines(x=tumor_drift, ymin=0, ymax=tumor_freq, color='#FF00FF', linestyle='--', linewidth=2, zorder=4)
    plt.hlines(y=tumor_freq, xmin=0, xmax=tumor_drift, color='#FF00FF', linestyle='--', linewidth=2, zorder=4)

    # Styling
    plt.title('PPT-Bio: Acoustic Resonance Targeting for DNA Restoration', fontsize=14, pad=20)
    plt.xlabel('Geometric Drift / Hydrostatic Misalignment (%)', fontsize=12)
    plt.ylabel('Restoration Wave Frequency (THz)', fontsize=12)
    
    plt.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    calculate_resonance_restoration()