import numpy as np
import matplotlib.pyplot as plt

# PPT-Atoms Validation Suite v1.0.0 & PPT-Bio
# Script: Dynamic_Resonance_Curing_Simulation.py
# Author: Vladimir Milosevic
# Theory: Plasma Pressure Theory (PPT) 3.0
# Description: Simulates the dynamic cybernetic feedback loop of acoustic DNA restoration.

def simulate_dynamic_resonance_cure():
    print("--- PPT - Atoms: PPT 3.0: Dynamic Resonance Curing Simulation ---")

    # 1. PPT 3.0 CONSTANTS
    E_healthy = 0.15  # eV (Baseline hydrostatic pinning pressure of H-bond)
    h_eV_s = 4.135667696e-15  # Planck's constant (Medium's Viscoelastic Harmonic Constant)
    
    # Treatment Parameters
    treatment_time_minutes = 60
    dt = 0.1  # Time step resolution
    time_steps = np.arange(0, treatment_time_minutes, dt)

    # 2. PATIENT INITIAL STATE
    current_drift = 45.0  # Starting at 45% (Aggressive Carcinogenic Misalignment)
    drift_history = []
    frequency_history_THz = []

    # 3. THE CURE: CYBERNETIC FEEDBACK LOOP SIMULATION
    # The machine injects targeted acoustic energy, closing the geometric gap over time.
    # The healing rate depends on the tissue's viscoelastic resistance (damping).
    healing_rate_constant = 0.08  

    print("\nInitiating Cybernetic Terahertz Sweep...")
    print(f"Targeting Initial Carcinogenic Drift: {current_drift}%")
    print("-" * 65)
    print(f"{'Time (Mins)':<15} | {'Remaining Drift (%)':<22} | {'Machine Output (THz)'}")
    print("-" * 65)

    for t in time_steps:
        # A. Calculate current pressure deficit
        # The deficit equals the lost geometric overlap volume
        current_deficit_eV = E_healthy * (current_drift / 100)**2
        
        # B. Calculate the exact frequency needed AT THIS MILLISECOND
        # f = E / h
        current_freq_THz = (current_deficit_eV / h_eV_s) / 1e12
        
        # C. Record data for visual proof
        drift_history.append(current_drift)
        frequency_history_THz.append(current_freq_THz)
        
        # Print terminal updates at specific intervals (every 15 minutes)
        if round(t, 1) % 15.0 == 0.0:
            print(f"{t:<15.1f} | {current_drift:<22.2f} | {current_freq_THz:.3f} THz")
        
        # D. Apply the wave (The bond absorbs the resonant energy and shifts back)
        # The drift decays exponentially as it locks back into the healthy baseline
        current_drift = current_drift - (healing_rate_constant * current_drift * dt)

    # Print final state
    print(f"{treatment_time_minutes:<15.1f} | {current_drift:<22.4f} | {frequency_history_THz[-1]:.3f} THz")
    print("-" * 65)
    print("Treatment Complete: DNA Lattice Hydrostatically Restored.")

    # 4. HIGH-VISIBILITY VISUAL PROOF
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8), sharex=True)

    # Top Plot: The Structural Restoration (The "Cure")
    ax1.plot(time_steps, drift_history, color='#00FFFF', linewidth=3, zorder=3)
    ax1.axhline(0, color='gray', linestyle='--', zorder=2)
    ax1.fill_between(time_steps, drift_history, 0, color='#00FFFF', alpha=0.15)
    ax1.set_ylabel('Geometric Drift (%)', fontsize=12)
    ax1.set_title('Targeted DNA Lattice Restoration Over Time', fontsize=14, pad=10)
    
    # Annotations
    bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.9)
    ax1.text(treatment_time_minutes * 0.8, 40, 'Initial Tumor State', color='#e63946', bbox=bbox_props, fontweight='bold', zorder=4)
    ax1.text(treatment_time_minutes * 0.8, 5, 'Restored Baseline (0%)', color='black', bbox=bbox_props, fontweight='bold', zorder=4)
    ax1.grid(True, linestyle='--', alpha=0.3)

    # Bottom Plot: The Machine's Output (The "Sweep")
    ax2.plot(time_steps, frequency_history_THz, color='#FF00FF', linewidth=3, zorder=3)
    ax2.fill_between(time_steps, frequency_history_THz, 0, color='#FF00FF', alpha=0.15)
    ax2.set_ylabel('Machine Output Freq (THz)', fontsize=12)
    ax2.set_xlabel('Treatment Time (Minutes)', fontsize=12)
    ax2.set_title('Cybernetic Frequency Sweeping (Walking the Bond Back)', fontsize=14, pad=10)
    ax2.grid(True, linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_dynamic_resonance_cure()