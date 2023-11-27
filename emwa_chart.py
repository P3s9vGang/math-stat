from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# TODO - Цвета area
def emwa_chart(url):
    table = pd.read_excel(f'{url}')
    x = table.values[:, 0]
    y = table.values[:, 1]
    y_list = np.array(y).tolist()
    print(y_list)
    alpha = 0.2
    y_ewma, y_limit_up, y_limit_down = [], [], []
    z_av = sum(y_list) / len(y_list)
    for i in range(len(y_list)):
        if i == 0:
            y_ewma.append(alpha * y_list[i] + (1 - alpha) * z_av)
        else:
            y_ewma.append(alpha * y_list[i] + (1 - alpha) * y_ewma[i - 1])
    for i in range(len(y_list)):
        limit = 1.95 * 3 * sqrt(((alpha) / (2 - alpha)) * (1 - (1 - alpha) ** ((2 * (i + 1)))))
        y_limit_up.append(z_av + limit)
        y_limit_down.append(z_av - limit)

    def check_points(y_ewma, y_limit_up, y_limit_down):
        for i in range(len(y_ewma)):
            if y_ewma[i] >= y_limit_up[i] or y_ewma[i] <= y_limit_down[i]:
                plt.scatter(i + 1, y_ewma[i], s=300, c='red', marker='X')
            else:
                plt.scatter(i + 1, y_ewma[i], s=120, c='blue', marker='o')
    plt.figure(figsize=(15, 7))
    plt.plot(x, y_ewma, color='blue', label='EWMA')
    plt.plot(x, y_limit_up, color='green', label='UCL', linestyle='--')
    plt.plot(x, y_limit_down, color='green', label='LCL', linestyle='--')
    plt.scatter(x, y, s=120, c='orange', marker='*')
    plt.axhline(y=z_av, color='red', linestyle='-', label='AVG')
    check_points(y_ewma, y_limit_up, y_limit_down)
    plt.xlabel('Axe x', fontsize=16)
    plt.ylabel('Axe y', fontsize=16)
    plt.xlim([0.8, len(y) + 0.2])
    plt.title('EWMA Chart', fontsize=30)
    plt.show()