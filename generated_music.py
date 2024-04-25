import librosa
import numpy as np
from scipy.signal import find_peaks

# Load the audio file
y, sr = librosa.load("music.mp3")

# Perform a short-time Fourier transform (STFT) to convert the audio from the time domain to the frequency domain
D = librosa.stft(y)

# Compute the magnitude of the STFT
spectrogram = np.abs(D)

# Find the peak frequency for each time frame
peak_frequencies = np.argmax(spectrogram, axis=0)

# Convert the peak frequencies to Hz
peak_frequencies_hz = librosa.fft_frequencies(sr=sr)[peak_frequencies]

# Print the peak frequencies
print(peak_frequencies_hz)
