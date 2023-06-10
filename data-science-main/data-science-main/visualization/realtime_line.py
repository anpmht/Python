import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
import numpy as np
from math import sin
import pandas as pd

df = pd.read_csv("data_2.csv")

a = 0
fig = plt.figure(figsize=(12, 3))
x = [0]
y = [0]
 
ln, = plt.plot(x, y, '-')
plt.xlabel("time")
plt.ylabel("mv")
plt.title("strain gauge real time data")
# plt.axis([0, 10000, -1.5, 1.5])       # manual scaling
 
def update(frame):
    x.append(x[-1] + 1)
    global a
    k = a/90
    y.append(df["left"][a])
    if len(x)>100:
        x.pop(0)  
        y.pop(0)  
    ln.set_data(x, y)
    fig.gca().relim()
    fig.gca().autoscale_view()           # autoscaling
    a = a+1
    return ln
 
animation = FuncAnimation(fig, update, frames = 500, interval = 1, blit  = False)
# animation.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30)
plt.show()