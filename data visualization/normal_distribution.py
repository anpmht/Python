import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load data from CSV file
data = pd.read_csv('data_2.csv')

# Calculate mean and standard deviation
mu = np.mean(data['left'])
sigma = np.std(data['left'])

# Create x-axis values
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

# Create normal distribution
y = norm.pdf(x, mu, sigma)

# Plot histogram and normal distribution
fig, ax = plt.subplots()
ax.hist(data['left'], bins=50, density=True, alpha=0.6, label='Data')
ax.plot(x, y, 'r', label='Normal Distribution')
ax.set_xlabel('Value')
ax.set_ylabel('Probability Density')
ax.set_title('Normal Distribution Example')
ax.legend()

# Display plot
plt.show()
