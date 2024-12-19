import numpy as np
import math
import matplotlib.pyplot as plt

coordinates = np.random.randint(1, 21, size=(30, 2))

x = coordinates[:, 0]
y = coordinates[:, 1]
K = [15, 7.5]
k_X = K[0]
k_y = K[1]

eo_distances = []

def euclidean_distance(x, y):
    for i in range(len(x)):
        distance_x = x[i] - k_X
        distance_y = y[i] - k_y
        distance = math.sqrt(distance_x**2 + distance_y**2)
        eo_distances.append((distance, x[i], y[i]))


euclidean_distance(x, y)

eo_distances.sort(key=lambda t: t[0])

smallest_15 = eo_distances[:12]

closest_x = [coord[1] for coord in smallest_15]
closest_y = [coord[2] for coord in smallest_15]

plt.scatter(x, y, color='blue')
plt.scatter(closest_x, closest_y, color='yellow')
plt.scatter(K[0], K[1], color='red')
plt.title("Rastgele Koordinatlar ve En Yakın 15 Nokta")
plt.xlabel("X Koordinatları")
plt.ylabel("Y Koordinatları")
plt.grid(True)
plt.xlim(0, 21)
plt.ylim(0, 21)  #

plt.show()

