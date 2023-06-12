import pandas as pd
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('data_2.csv')

# Define filter parameters
fs = 300 # Sampling frequency (Hz)
fc = 10 # Cutoff frequency (Hz)
order = 4 # Filter order

# Create low pass filter
nyq = 0.5 * fs
cutoff = fc / nyq
b, a = butter(order, cutoff, btype='low', analog=False)

# Apply filter to data
left_filter = filtfilt(b, a, data['left'])
right_filter = filtfilt(b, a, data['right'])
# Plot original and filtered data
fig, ax = plt.subplots()
ax.plot(data['left'][0:20000], label='Original Data')
ax.plot(left_filter, label='left filter')
ax.set_xlabel('Sample Number')
ax.set_ylabel('Signal Amplitude')
ax.set_title('Low Pass Filter Example')
ax.legend()

# Save filtered data to CSV file
filtered_data_df = pd.DataFrame({'Filtered Data': left_filter})
filtered_data_df.to_csv('filtered_data_2.csv', index=False)

# Display plot
plt.show()
