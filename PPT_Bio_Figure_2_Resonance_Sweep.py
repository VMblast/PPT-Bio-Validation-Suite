import numpy as np
import matplotlib.pyplot as plt

# PPT-Atoms Validation Suite v1.0.0 PPT-Bio
# Script: PPT_Bio_Figure_2_Resonance_Sweep.py
# Author: Vladimir Milosevic
# Theory: Plasma Pressure Theory (PPT) 3.0
# Description: Generates Figure 2 (Dual-Axis) for the PPT-Bio paper, plotting DNA drift vs machine frequency over time.

def generate_figure_2():
    print("--- PPT-BIO: GENERATING FIGURE 2 (RESONANCE SWEEP) ---")

    # 1. PPT 3.0 CONSTANTS & INITIAL STATE
    E_healthy = 0.15          # Baseline H-bond pinning pressure (eV)
    h_eV_s = 4.135667696e-15  # Viscoelastic resistance factor (Planck)
    healing_rate = 0.08       # Mechanical lattice absorption rate
    
    # Time domain (60 minute treatment, high resolution)
    time = np.linspace(0, 60, 300)

    # 2. ANALYTICAL EXPONENTIAL DECAY
    # Drift naturally decays exponentially under constant resonant pressure
    drift = 45.0 * np.exp(-healing_rate * time)
    
    # 3. HYDROSTATIC DEFICIT & TARGET FREQUENCY
    deficit = E_healthy * (drift / 100)**2
    freq_THz = (deficit / h_eV_s) / 1e12

    # --- HIGH-VISIBILITY DUAL-AXIS PLOTTING ---
    fig, ax1 = plt.subplots(figsize=(11, 6.5))

    # Plot 1: Geometric Drift (Cyan)
    color1 = '#00FFFF'
    ax1.set_xlabel('Treatment Time (Minutes)', fontsize=12)
    ax1.set_ylabel('Geometric Drift Misalignment (%)', color=color1, fontsize=12)
    curve1 = ax1.plot(time, drift, color=color1, linewidth=4, label='DNA Lattice Drift (%)', zorder=4)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, linestyle='--', alpha=0.3)

    # Highlight High-Danger Zone
    ax1.axhspan(30, 60, color='#e63946', alpha=0.15)
    bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.9)
    ax1.text(5, 35, 'High-Danger Carcinogenic Zone', color='black', bbox=bbox_props, fontweight='bold', fontsize=10, zorder=5)

    # Plot 2: Machine Output (Magenta) - Twin Axis
    ax2 = ax1.twinx()
    color2 = '#FF00FF'
    ax2.set_ylabel('Machine Output Frequency (THz)', color=color2, fontsize=12)
    curve2 = ax2.plot(time, freq_THz, color=color2, linewidth=3, linestyle='--', label='Required Restoration Sweep (THz)', zorder=3)
    ax2.tick_params(axis='y', labelcolor=color2)

    # Aesthetics & Legends
    plt.title('Figure 2: The Cybernetic Resonance Sweep & DNA Restoration', fontsize=14, pad=20)
    
    # Combine legends from both axes to prevent overlapping
    lns = curve1 + curve2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc='upper right', frameon=True, facecolor='white', framealpha=0.9)

    fig.tight_layout()
    plt.savefig('PPT_Bio_Figure_2.png', dpi=300, bbox_inches='tight')
    print("SUCCESS: 'PPT_Bio_Figure_2.png' has been saved at 300 DPI for publication.")
    plt.show()

if __name__ == "__main__":
    generate_figure_2()