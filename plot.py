
# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


# Creating dataset
y = [2003, 1976, 2001, 1915, 2000, 1993, 2004, 1973, 1931, 1939,
     1965, 2005, 1962, 2006, 1960, 1929, 1970, 1967, 2004, 1958, 2005]
x = [8450, 9600, 11250,
     9550, 14260, 14115, 10084, 10382, 6120, 7420, 11200, 11924, 12968, 10652, 10382, 6120, 7420, 11200, 11924, 12968, 10652]
z = [208500,
     181500,
     223500,
     140000,
     250000,
     143000,
     307000,
     200000,
     129900,
     118000,
     129500,
     345000,
     144000,
     279500,
     200000,
     129900,
     118000,
     129500,
     345000,
     144000,
     279500]

# Creating figure
fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

# Creating plot
ax.scatter3D(x, y, z, color="black")

ax.set_ylabel('Year Build')
ax.set_zlabel('House price')
ax.set_xlabel('sq. Feet')

plt.title("With two Features")

# show plot
plt.show()
