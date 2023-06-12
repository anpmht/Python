import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('data_2.csv')

# Number of sample points
N = len(data['left'])

# Sampling frequency
fs = 333

# Time interval
t = 1/fs

# Create time array
time = np.linspace(0, N*t, N)

# Compute FFT
yf = np.fft.fft(data['left'])

# Compute frequency axis
xf = np.linspace(10, 100, 100)

# Plot FFT
fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:100]))
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Magnitude')
ax.set_title('FFT Example')

# Display plot
plt.show()
