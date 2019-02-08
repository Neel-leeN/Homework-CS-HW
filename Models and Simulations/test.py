import numpy as np
from matplotlib.pylab import plt #load plot library
# indicate the output of plotting function is printed to the notebook
# %matplotlib inline 
from Roulettte.py import test


def create_random_walk():
    x = np.random.choice([-1,1],size=100, replace=True) # Sample with replacement from (-1, 1)
    return np.cumsum(x) # Return the cumulative sum of the elements
X = create_random_walk()
Y = create_random_walk()
Z = create_random_walk()

# Plotting functionality starts here
plt.plot(test[0])
plt.plot(test[1])
plt.plot(test[2])
plt.show()