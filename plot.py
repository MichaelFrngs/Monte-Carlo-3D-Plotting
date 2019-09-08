import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def ShapeOf3dFunction(x,y):
    output = (x**2+y**2)**0.5
    return output

NumberOfPoints = 100000

i = 0
x_list = []
y_list = []
result_list = []
while i < NumberOfPoints:
    x = np.random.uniform(low=-2, high=2, size=(1,1))[0][0]
    y = np.random.uniform(low=-2, high=2, size=(1,1))[0][0]
    
    
    x_list.append(x)
    y_list.append(y)
    
    output = ShapeOf3dFunction(x,y)*1000
    result_list.append(output)

    i = i+1

ax = plt.axes(projection='3d')    
ax.scatter(x_list, y_list, result_list, 'gray',s= .01)

import plotly.graph_objects as go
fig = go.Figure(data=[go.Mesh3d(x=x_list, y=y_list, z=result_list, color='lightpink', opacity=0.50)])
fig.show()

