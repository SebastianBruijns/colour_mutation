import numpy as np
import matplotlib.pyplot as plt


n, m = 450, 800
steps = [1, 10, 25, 40, 55, 70, 85]
propagation_chance = 0.5
step_size = 0.05

colours = np.zeros((n, m, 3))
colours[n // 2, m // 2] = 0.5

neigbhours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for step in range(steps[-1]):
	print(step)
	xs, ys, _ = np.where(colours != 0)
	for x, y in zip(xs, ys):
		for neigh in neigbhours:
			if 0 < x + neigh[0] < n and 0 < y + neigh[1] < m:
				if (colours[x + neigh[0], y + neigh[1]] == np.zeros(3)).all():
					if np.random.rand() < propagation_chance:
						colours[x + neigh[0], y + neigh[1]] = colours[x, y] + np.random.rand(3) * step_size
	colours = colours % 1
	if step in steps:
		plt.imshow(colours)
		plt.show()