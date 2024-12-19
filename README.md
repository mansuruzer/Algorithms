

Algorithm of the Code File:

1- Generate 30 random points within the range of 1 to 20 for both x and y coordinates.
2- Determine the K point: This is the reference point (K-NN stands for K-Nearest Neighbors).
3- Define a function to calculate the Euclidean distance between the K point and the random points.
4- Store the coordinates and distances in a list.
5- Sort the list by distances, so that the nearest points to K are ordered first.
6- Select the nearest 15 points based on the sorted distances.
7- Plot the graph:
The graph shows the random points and the nearest 15 points, each colored differently.
In the actual K-NN algorithm, points are typically classified and labeled, but in this file, different colors are used to distinguish between the points, and there is no explicit classification or labeling.
8-Display the graph using matplotlib.






