"""
ECG Loader Animation Generator for Website
Creates a slow, smooth red ECG waveform with:
- Reduced R and S peak amplitudes
- Longer T wave
- Negative T wave position
- More space between heartbeats
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Animation parameters
duration = 10.0  # seconds for one complete cycle (slower)
fps = 30
frames = int(duration * fps)

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 2.5), facecolor='white')
ax.set_xlim(0, 10)
ax.set_ylim(-0.3, 0.5)
ax.axis('off')

# Generate ECG waveform with modifications
def generate_ecg_wave(t):
    """Generate a smooth ECG waveform with requested modifications"""
    ecg = np.zeros_like(t)
    
    for i, time in enumerate(t):
        # Normalize time to [0, 1.5] for one heartbeat with more spacing
        phase = (time % 1.5) / 1.5  # Extended to 1.5 for more space between beats
        
        # P wave (0.0 - 0.1)
        if 0.0 <= phase < 0.1:
            ecg[i] = 0.08 * np.sin(2 * np.pi * (phase - 0.0) / 0.1)
        
        # PR segment (0.1 - 0.133)
        elif 0.1 <= phase < 0.133:
            ecg[i] = 0.0
        
        # Q wave (0.133 - 0.15)
        elif 0.133 <= phase < 0.15:
            ecg[i] = -0.03 * np.sin(2 * np.pi * (phase - 0.133) / 0.017)
        
        # R wave (0.15 - 0.183) - REDUCED amplitude to 0.35
        elif 0.15 <= phase < 0.183:
            ecg[i] = 0.35 * np.sin(2 * np.pi * (phase - 0.15) / 0.033)
        
        # S wave (0.183 - 0.2) - REDUCED amplitude to 0.05
        elif 0.183 <= phase < 0.2:
            ecg[i] = -0.05 * np.sin(2 * np.pi * (phase - 0.183) / 0.017)
        
        # ST segment (0.2 - 0.267)
        elif 0.2 <= phase < 0.267:
            ecg[i] = 0.0
        
        # T wave (0.267 - 0.467) - LONGER duration and NEGATIVE
        elif 0.267 <= phase < 0.467:
            ecg[i] = -0.12 * np.sin(2 * np.pi * (phase - 0.267) / 0.2)
        
        # Extended baseline (0.467 - 1.0) - MORE SPACE between beats
        else:
            ecg[i] = 0.0
    
    return ecg + 0.1  # Offset to center

# Generate full ECG signal (one lead)
t_full = np.linspace(0, 10, 1500)
ecg_full = generate_ecg_wave(t_full)

# Initialize line with thicker width for better visibility on website
line, = ax.plot([], [], color='#DC143C', linewidth=2.5, antialiased=True)

def init():
    line.set_data([], [])
    return line,

def animate(frame):
    # Calculate how much of the wave to show (slower progression)
    progress = frame / frames
    end_point = int(progress * len(t_full))
    
    # Update line data
    line.set_data(t_full[:end_point], ecg_full[:end_point])
    return line,

# Create animation
anim = FuncAnimation(fig, animate, init_func=init, frames=frames, 
                     interval=1000/fps, blit=True, repeat=True)

# Save as GIF with optimization for web
writer = PillowWriter(fps=fps)
print("Generating ECG loader animation...")
anim.save('ecg_loader.gif', writer=writer, dpi=100)

print("✓ ECG loader animation saved as 'ecg_loader.gif'")
print(f"Duration: {duration}s | FPS: {fps}")
print("Features:")
print("  - Reduced R peak (0.35) and S peak (0.05)")
print("  - Longer T wave duration (200ms)")
print("  - Negative T wave position")
print("  - Increased spacing between heartbeats")
plt.close()
