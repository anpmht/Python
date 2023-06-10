import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


plot_styles = ['seaborn-dark', 'dark_background', 'seaborn-pastel', 'seaborn-colorblind', 'tableau-colorblind10', 'seaborn-notebook', 'seaborn-dark-palette', 'grayscale', 'seaborn-poster', 'seaborn', 'bmh', 'seaborn-talk', 'seaborn-ticks', '_classic_test', 'ggplot', 'seaborn-white', 'classic', 'Solarize_Light2', 'seaborn-paper', 'fast', 'fivethirtyeight', 'seaborn-muted', 'seaborn-whitegrid', 'seaborn-darkgrid', 'seaborn-bright', 'seaborn-deep']
plt.style.use(plot_styles[11])
matplotlib.rcParams.update({'font.size': 10, 'font.family': 'times new roman'}) # defines defaud font size and family


df = pd.read_csv("data_2.csv")

fig = plt.figure(figsize=(10, 5))    # figure 
# plt.xlim(0, 100)
# plt.ylim(0, 1000)
plt.scatter(df["left"][0:100],df["time"][0:100],s=30,color = "red")
plt.grid(True)
plt.title("left gauge",fontsize=15)
plt.xlabel("time",fontsize=15)
plt.ylabel("mv",fontsize=15)         
plt.legend(loc=1)# legend location, useful for multiplot chart
plt.show() 