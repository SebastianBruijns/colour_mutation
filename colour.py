import numpy as np
import matplotlib.pyplot as plt
import time
import imageio

# @profile
def call():
    # record:
    # n, m = 1200 * 8, 1200 * 8
    # steps = 750 * 16
    n, m = 4000, 4000
    steps = 2500
    images = []

    propagation_chance = 0.2
    step_size = 0.05
    np.random.seed(6)

    colours = np.ones((n, m, 3))
    # colours[n // 2, m // 2] = [0.76, 0.76, 0.24]
    colours[n // 4, m // 4] = [0.76, 0.76, 0.24]
    colours[2 * n // 5, 3 * m // 5] = [0.24, 0.76, 0.24]
    colours[3 * n // 5, 2 * m // 5] = [0.76, 0.24, 0.24]
    colours[3 * n // 4, 3 * m // 4] = [0.24, 0.76, 0.76]

    outer_cells = [(n // 4, m // 4), (3 * n // 5, 2 * m // 5), (2 * n // 5, 3 * m // 5), (3 * n // 4, 3 * m // 4)]
    neigbhours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    spread = 0.02

    def dist(): return np.random.beta(1, 1, 3) * spread - spread / 2
    rand_nums = np.random.normal(0, np.sqrt(1 / 12 * (2 * spread) ** 2), (n * m, 3))
    compare = np.ones(3)

    rand_counter = 0
    for step in range(steps):
        # print(step, len(outer_cells))
        next_cells = []
        for x, y in outer_cells:
            counter = 0
            for neigh in neigbhours:
                if 0 <= x + neigh[0] < n and 0 <= y + neigh[1] < m:
                    if (colours[x + neigh[0], y + neigh[1]] == 1).all():
                        counter += 1
                        if np.random.rand() < propagation_chance:
                            colours[x + neigh[0], y + neigh[1]] = colours[x, y] + rand_nums[rand_counter]
                            rand_counter += 1
                            counter -= 1
                            next_cells.append((x + neigh[0], y + neigh[1]))
            if counter >= 1:
                next_cells.append((x, y))
        outer_cells = next_cells
        colours = np.clip(colours, 0, 1)
        # colours[colours < 0] += 1 # doesn't work as well, leads to stark changes and bright colours. Maybe one needs to loop differently in RGB?
        # colours[colours > 1] -= 1
        if step % 10 == 0:
            print(step)
            plt.figure(figsize=(12, 12))
            plt.imshow(colours, vmin=0, vmax=1)
            plt.axis('off')
            plt.tight_layout()
            plt.savefig("q " + str(1 + step))
            images.append("q " + str(1 + step))
            plt.close()


    return images

# files = call()

files = ['q 1', 'q 11', 'q 21', 'q 31', 'q 41', 'q 51', 'q 61', 'q 71', 'q 81', 'q 91', 'q 101', 'q 111', 'q 121', 'q 131', 'q 141', 'q 151', 'q 161', 'q 171', 'q 181', 'q 191', 'q 201', 'q 211', 'q 221', 'q 231', 'q 241', 'q 251', 'q 261', 'q 271', 'q 281', 'q 291', 'q 301', 'q 311', 'q 321', 'q 331', 'q 341', 'q 351', 'q 361', 'q 371', 'q 381', 'q 391', 'q 401', 'q 411', 'q 421', 'q 431', 'q 441', 'q 451', 'q 461', 'q 471', 'q 481', 'q 491', 'q 501', 'q 511', 'q 521', 'q 531', 'q 541', 'q 551', 'q 561', 'q 571', 'q 581', 'q 591', 'q 601', 'q 611', 'q 621', 'q 631', 'q 641', 'q 651', 'q 661', 'q 671', 'q 681', 'q 691', 'q 701', 'q 711', 'q 721', 'q 731', 'q 741', 'q 751', 'q 761', 'q 771', 'q 781', 'q 791', 'q 801', 'q 811', 'q 821', 'q 831', 'q 841', 'q 851', 'q 861', 'q 871', 'q 881', 'q 891', 'q 901', 'q 911', 'q 921', 'q 931', 'q 941', 'q 951', 'q 961', 'q 971', 'q 981', 'q 991', 'q 1001', 'q 1011', 'q 1021', 'q 1031', 'q 1041', 'q 1051', 'q 1061', 'q 1071', 'q 1081', 'q 1091', 'q 1101', 'q 1111', 'q 1121', 'q 1131', 'q 1141', 'q 1151', 'q 1161', 'q 1171', 'q 1181', 'q 1191', 'q 1201', 'q 1211', 'q 1221', 'q 1231', 'q 1241', 'q 1251', 'q 1261', 'q 1271', 'q 1281', 'q 1291', 'q 1301', 'q 1311', 'q 1321', 'q 1331', 'q 1341', 'q 1351', 'q 1361', 'q 1371', 'q 1381', 'q 1391', 'q 1401', 'q 1411', 'q 1421', 'q 1431', 'q 1441', 'q 1451', 'q 1461', 'q 1471', 'q 1481', 'q 1491', 'q 1501', 'q 1511', 'q 1521', 'q 1531', 'q 1541', 'q 1551', 'q 1561', 'q 1571', 'q 1581', 'q 1591', 'q 1601', 'q 1611', 'q 1621', 'q 1631', 'q 1641', 'q 1651', 'q 1661', 'q 1671', 'q 1681', 'q 1691', 'q 1701', 'q 1711', 'q 1721', 'q 1731', 'q 1741', 'q 1751', 'q 1761', 'q 1771', 'q 1781', 'q 1791', 'q 1801', 'q 1811', 'q 1821', 'q 1831', 'q 1841', 'q 1851', 'q 1861', 'q 1871', 'q 1881', 'q 1891', 'q 1901', 'q 1911', 'q 1921', 'q 1931', 'q 1941', 'q 1951', 'q 1961', 'q 1971', 'q 1981', 'q 1991', 'q 2001', 'q 2011', 'q 2021', 'q 2031', 'q 2041', 'q 2051', 'q 2061', 'q 2071', 'q 2081', 'q 2091', 'q 2101', 'q 2111', 'q 2121', 'q 2131', 'q 2141', 'q 2151', 'q 2161', 'q 2171', 'q 2181', 'q 2191', 'q 2201', 'q 2211', 'q 2221', 'q 2231', 'q 2241', 'q 2251', 'q 2261', 'q 2271', 'q 2281', 'q 2291', 'q 2301', 'q 2311', 'q 2321', 'q 2331', 'q 2341', 'q 2351', 'q 2361', 'q 2371', 'q 2381', 'q 2391', 'q 2401', 'q 2411', 'q 2421', 'q 2431', 'q 2441', 'q 2451', 'q 2461', 'q 2471', 'q 2481', 'q 2491']

images = []
for filename in files[::4]:
    images.append(imageio.v2.imread(filename + '.png'))
imageio.mimsave('colours.gif', images, format='GIF', duration=80, loop=0)