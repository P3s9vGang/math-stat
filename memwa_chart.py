from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def memwa_chart(url):
    table = pd.read_excel(f'{url}')
    # how many columns in table
    list_of_columns = []
    for i in range(len(table.columns)):
        list_of_columns.append(table.values[:, i])
    x = list(range(1, len(list_of_columns[0]) + 1))
    list_of_columns = np.array(list_of_columns).transpose()
    lamda = 0.2
    L = 1
    avg_list = []
    memwa_points = []
    # average of first 10 elements of avg_list
    for i in list_of_columns:
        cur_list = []
        for cur in i:
            cur_list.append(cur)
        avg_list.append(sum(cur_list) / len(cur_list))
    sum_avg = 0
    for i in range(len(avg_list) // 2):
        sum_avg += avg_list[i]
    avg = sum_avg / (len(avg_list) // 2)
    for i in range(len(list_of_columns)):
        if i == 0: # TODO - Узнать какой лучше начальный коэффициент
            memwa_points.append(lamda * avg + (1 - lamda) * avg_list[i])
            continue
        memwa_points.append(lamda * avg_list[i] + (1 - lamda) * memwa_points[i - 1])
    u = sum(memwa_points) / len(memwa_points)
    ucl = []
    lcl = []
    sigma_list = []
    l = []
    for i in range(len(list_of_columns)):
        n = len(list_of_columns[i])
        sigma = np.var(list_of_columns[i]) * n / (n - 1) if n > 1 else np.var(list_of_columns[i])
        sigma_list.append(sigma)
    sigma_avg = sum(sigma_list) / len(sigma_list)
    if sigma_avg == 0:
        l_new = []
        for i in list_of_columns:
            for j in i:
                l_new.append(j)
        sigma_avg = np.var(l_new) / 2
    sigma_avg /= 2
    for i in range(len(list_of_columns)):
        if i == 0:
            sigma_i = L * sigma_avg * sqrt(((lamda) / (2 - lamda)) * (1 - (1 - lamda) ** ((2 * (i + 1)))))
        else:
            sigma_i = L * sigma_avg * sqrt(((lamda) / (2 - lamda)) * (1 - (1 - lamda) ** ((2 * (i + 1)))))
        l.append(sqrt(sigma_i))
        ucl.append(u + sqrt(sigma_i))
        lcl.append(u - sqrt(sigma_i))
    def check_points(y_ewma, y_limit_up, y_limit_down):
        for i in range(len(y_ewma)):
            if y_ewma[i] >= y_limit_up[i] or y_ewma[i] <= y_limit_down[i]:
                plt.scatter(i + 1, y_ewma[i], s=300, c='red', marker='X')
            else:
                plt.scatter(i + 1, y_ewma[i], s=120, c='blue', marker='o')
    plt.figure(figsize=(15, 7))
    plt.plot(x, memwa_points, color='blue', label='EWMA')
    plt.plot(x, ucl, color='green', label='UCL', linestyle='--')
    plt.plot(x, lcl, color='green', label='LCL', linestyle='--')
    plt.axhline(y=u, color='red', linestyle='-', label='AVG')
    check_points(memwa_points, ucl, lcl)
    plt.xlabel('Axe x', fontsize=16)
    plt.ylabel('Axe y', fontsize=16)
    plt.xlim([0.8, len(memwa_points) + 0.2])
    plt.title('MEWMA Chart', fontsize=30)
    plt.show()

