import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from scipy.signal import butter, filtfilt
# Read data from CSV file

df = pd.read_csv('data_2.csv')
df["right"] = df['right']*-1
# Define filter parameters
fs = 300 # Sampling frequency (Hz)
fc = 5 # Cutoff frequency (Hz)
order = 3 # Filter order

# Create low pass filter
nyq = 0.5 * fs
cutoff = fc / nyq
b, a = butter(order, cutoff, btype='low', analog=False)

# Apply filter to data
left_filter = filtfilt(b, a, df['left'])
right_filter = filtfilt(b, a, df['right'])
df['filtered_left'] = left_filter
df['filtered_right'] = right_filter
# Plot original and filtered data
print(df)
# Create figure and axis objects
fig, ax = plt.subplots()

# Initialize plot with first data point
x_data = [df['time'][0]]
y_left = [df['left'][0]]
y_right = [df['right'][0]]
y_filtered_left = [df['filtered_left'][0]]
y_filtered_right = [df['filtered_right'][0]]

#plot the data
line_left, = ax.plot(x_data, y_left, label='Left')
line_right, = ax.plot(x_data, y_right, label='Right')
filtered_left_line, = ax.plot(x_data, y_filtered_left, label='Left_filtered')
filtered_right_line, = ax.plot(x_data, y_filtered_right, label='right_filtered')

ax.legend()

# Define update function
def update(frame):
    # Read new data point from CSV file
    new_data = df.iloc[frame]
    
    # Add new data point to x and y data lists
    x_data.append(new_data['time'])
    y_left.append(new_data['left'])
    y_right.append(new_data['right'])
    y_filtered_left.append(new_data['filtered_left'])
    y_filtered_right.append(new_data['filtered_right'])
    
    # Remove oldest data point if number of data points exceeds 1000
    if len(x_data) > 500:
        x_data.pop(0)
        y_left.pop(0)
        y_right.pop(0)
        y_filtered_left.pop(0)
        y_filtered_right.pop(0)

    # Update plot with new data
    line_left.set_data(x_data, y_left)
    line_right.set_data(x_data, y_right)
    filtered_left_line.set_data(x_data, y_filtered_left)
    filtered_right_line.set_data(x_data, y_filtered_right)
    ax.relim()
    ax.autoscale_view()
    
    # Return plot objects
    return line_left, line_right, filtered_left_line, filtered_right_line

# Create animation object and show plot
animation = FuncAnimation(fig, update, frames=len(df), blit=False, interval=1)
plt.show()
animation.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30)