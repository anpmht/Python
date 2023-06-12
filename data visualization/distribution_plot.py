import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 2, 2.5, 3, 3.5, 4, 5])
ax = s.plot.kde()
plt.show()

#bandwidth specification
ax = s.plot.kde(bw_method=0.3)
plt.show()
ax = s.plot.kde(bw_method=3)
plt.show()

# defining evaluation points for the density plot
ax = s.plot.kde(ind=[1, 2, 3, 4, 5])
plt.show()

#plotting using dataframe
df = pd.DataFrame({
    'x': [1, 2, 2.5, 3, 3.5, 4, 5],
    'y': [4, 4, 4.5, 5, 5.5, 6, 6],
})
ax = df.plot.kde()
plt.show()

# bandwidth in dataframe
ax = df.plot.kde(bw_method=0.3)
plt.show()

# evaluation points for dataframe
ax = df.plot.kde(ind=[1, 2, 3, 4, 5, 6])
plt.show()