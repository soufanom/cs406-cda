import matplotlib.pyplot as plt
import numpy as np
# Generating two layers
layer1 = np.random.rand(10,10)
layer2 = np.random.rand(10,10)

print(layer1)
# Displaying the first layer
plt.imshow(layer1, cmap='GnBu', extent=(0, 10, 0, 10))
# Displaying the second layer on top with transparency
plt.imshow(layer2, cmap='hot', alpha=0.5, extent=(0, 10, 0, 10))
plt.show()