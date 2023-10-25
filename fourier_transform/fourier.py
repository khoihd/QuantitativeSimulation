import numpy as np
import matplotlib.pyplot as plt

# Create a sample signal
sample_rate = 1000  # Hz
t = np.arange(0, 1, 1/sample_rate)  # 1 second of data
frequency = 50  # Frequency of the signal (5 Hz)
signal = np.sin(2 * np.pi * frequency * t)

# Perform the Fourier transform
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(fft_result), 1/sample_rate)

# Plot the original signal and its frequency domain representation
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Original Signal")

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_result))
plt.title("Frequency Domain Representation")
plt.xlabel("Frequency (Hz)")

plt.tight_layout()
plt.show()
