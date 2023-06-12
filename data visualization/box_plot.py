import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

data = np.random.randn(25, 4)
df = pd.DataFrame(data, columns=list('ABCD'))
ax = df.plot.box()
plt.show()

age_list = [8, 10, 12, 14, 72, 74, 76, 78, 20, 25, 30, 35, 60, 85]
df = pd.DataFrame({"gender": list("MMMMMMMMFFFFFF"), "age": age_list})
ax = df.plot.box(column="age", by="gender", figsize=(10, 8))
plt.show()