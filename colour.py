import numpy as np
import matplotlib.pyplot as plt


n, m = 900, 1600
steps = 1200
propagation_chance = 0.2
step_size = 0.05

colours = np.ones((n, m, 3))
colours[n // 2, m // 2] = [0.8, 0.8, 0.2]

outer_cells = [(n // 2, m // 2)]
neigbhours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

saves = []

spread = 0.05


def dist(): np.random.beta(1, 1, 3) * spread - spread / 2


for step in range(steps):
    print(step)
    next_cells = []
    # saves.append(colours.copy())
    for x, y in outer_cells:
        counter = 0
        for neigh in neigbhours:
            if 0 <= x + neigh[0] < n and 0 <= y + neigh[1] < m:
                if (colours[x + neigh[0], y + neigh[1]] == np.ones(3)).all():
                    counter += 1
                    if np.random.rand() < propagation_chance:
                        colours[x + neigh[0], y + neigh[1]] = colours[x, y] + np.random.rand(3) * step_size - step_size / 2
                        counter -= 1
                        next_cells.append((x + neigh[0], y + neigh[1]))
        if counter >= 1:
            next_cells.append((x, y))
    outer_cells = next_cells
    colours = np.clip(colours, 0, 1)
    if (step % 10 == 0 and step > 900) or step % 100 == 0:
        plt.figure(figsize=(12, 12))
        plt.imshow(colours, vmin=0, vmax=1)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(str(step))
        plt.close()
