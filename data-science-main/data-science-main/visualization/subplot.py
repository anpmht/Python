import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data_2.csv")
fig, axes = plt.subplots(2, 2, figsize=(6, 6))

axes[0,0].scatter(df["left"][0:100], df["right"][0:100] )
axes[0,0].set_title("scatter")

axes[0,1].step(df["left"][0:100], df["right"][0:100], lw=2)
axes[0,1].set_title("step")

axes[1,0].bar(df["left"][0:100], df["right"][0:100], align="center", width=0.5, alpha=0.5)
axes[1,0].set_title("bar")

axes[1,1].fill_between( df["left"][0:100], df["right"][0:100],df["time"][0:100],color="green", alpha=0.5)
axes[1,1].set_title("fill_between")

plt.show()

fig = plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))
fig.tight_layout()
plt.show()