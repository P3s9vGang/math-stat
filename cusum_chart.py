from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def cusum_chart(url):
    table = pd.read_excel(f'{url}')
    # how many columns in table
    list_of_columns = []
    for i in range(len(table.columns)):
        list_of_columns.append(table.values[:, i])
    x = list(range(1, len(list_of_columns[0]) + 1))
    imr_list = []
    for i in range(1, len(list_of_columns[0])):
        imr_list.append(abs(list_of_columns[0][i - 1] - list_of_columns[0][i]))
    CL = sum(list_of_columns[0]) / len(list_of_columns[0])
    imr_avg = sum(imr_list) / len(imr_list)
    d3 = 1.128
    sigma = imr_avg / d3
    w = 0.0084 # TODO - Подобрать w
    u = CL
    UCL = 4 * sigma
    LCL = -4 * sigma
    uc_list, lc_list = [], []
    for i in range(0, len(list_of_columns[0])):
        if i == 0:
            uc_list.append(max(0, 0 + list_of_columns[0][i] - w - u))
            lc_list.append(min(0, 0 + list_of_columns[0][i] + w - u))
            continue
        uc_list.append(max(0, uc_list[i - 1] + list_of_columns[0][i] - w - u))
        lc_list.append(min(0, lc_list[i - 1] + list_of_columns[0][i] + w - u))

    def check_points(x_avg, UCLx, LCLx, shift=0):
        for i in range(len(x_avg)):
            if x_avg[i] >= UCLx or x_avg[i] <= LCLx:
                plt.scatter(i + 1 + shift, x_avg[i], s=300, c='red', marker='X')
            else:
                plt.scatter(i + 1 + shift, x_avg[i], s=120, c='blue', marker='o')

    plt.figure(figsize=(15, 7))
    plt.plot(x, uc_list, color='blue', label='EWMA')
    plt.plot(x, lc_list, color='blue', label='EWMA')
    plt.axhline(y=UCL, color='green', label='UCL', linestyle='--')
    plt.axhline(y=LCL, color='green', label='LCL', linestyle='--')
    plt.axhline(y=CL, color='green', label='LCL', linestyle='--')
    check_points(uc_list, UCL, LCL)
    check_points(lc_list, UCL, LCL)
    plt.xlabel('Axe x', fontsize=16)
    plt.ylabel('Axe y', fontsize=16)
    plt.xlim([0.8, len(list_of_columns[0]) + 0.2])
    plt.title('CUSUM', fontsize=30)
    plt.show()
