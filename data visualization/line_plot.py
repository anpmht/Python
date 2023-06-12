import pandas as pd
from matplotlib import pyplot as plt, rcParams
import matplotlib
import json 

plot_styles = ['seaborn-dark', 'dark_background', 'seaborn-pastel', 'seaborn-colorblind', 'tableau-colorblind10', 'seaborn-notebook', 'seaborn-dark-palette', 'grayscale', 'seaborn-poster', 'seaborn', 'bmh', 'seaborn-talk', 'seaborn-ticks', '_classic_test', 'ggplot', 'seaborn-white', 'classic', 'Solarize_Light2', 'seaborn-paper', 'fast', 'fivethirtyeight', 'seaborn-muted', 'seaborn-whitegrid', 'seaborn-darkgrid', 'seaborn-bright', 'seaborn-deep']
plt.style.use(plot_styles[8])
matplotlib.rcParams.update({'font.size': 10, 'font.family': 'times new roman'}) # defines defaud font size and family

df = pd.read_csv("data_2.csv")

fig = plt.figure(figsize=(10, 5))    # figure size
df["left"][0:100].plot(color='blue', linestyle='-', linewidth=0.5,              # '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
                marker='o', markerfacecolor='red', markersize=2,label="1 Hz")
plt.grid(True)
plt.title("left gauge",fontsize=15)
plt.xlabel("time",fontsize=15)
plt.ylabel("mv",fontsize=15)         
plt.legend(loc=1)# legend location, useful for multiplot chart
plt.show()                    

fig.savefig('Basic.png', dpi=300)


