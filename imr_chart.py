from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def x_mr_chart(url):
    table = pd.read_excel(f'{url}')
    # how many columns in table
    list_of_columns = []
    for i in range(len(table.columns)):
        list_of_columns.append(table.values[:, i])
    x = list(range(1, len(list_of_columns[0]) + 1))
    n = len(list_of_columns[0])
    imr_list = []
    for i in range(1, len(list_of_columns[0])):
        imr_list.append(abs(list_of_columns[0][i - 1] - list_of_columns[0][i]))
    CL = sum(list_of_columns[0]) / len(list_of_columns[0])
    imr_avg = sum(imr_list) / len(imr_list)
    E2 = 2.66
    D3 = 0
    D4 = 3.267
    UCLx = CL + E2 * imr_avg
    LCLx = CL - E2 * imr_avg
    UCLmr = D4 * imr_avg
    LCLmr = D3 * imr_avg

    def check_points(x_avg, UCLx, LCLx, shift=0):
        for i in range(len(x_avg)):
            if x_avg[i] >= UCLx or x_avg[i] <= LCLx:
                plt.scatter(i + 1 + shift, x_avg[i], s=300, c='red', marker='X')
            else:
                plt.scatter(i + 1 + shift, x_avg[i], s=120, c='blue', marker='o')

    plt.figure(figsize=(15, 7))
    plt.plot(x, list_of_columns[0], color='blue', label='EWMA')
    plt.axhline(y=UCLx, color='green', label='UCL', linestyle='--')
    plt.axhline(y=LCLx, color='green', label='LCL', linestyle='--')
    plt.axhline(y=CL, color='green', label='LCL', linestyle='--')
    check_points(list_of_columns[0], UCLx, LCLx)
    plt.xlabel('Axe x', fontsize=16)
    plt.ylabel('Axe y', fontsize=16)
    plt.xlim([0.8, len(list_of_columns[0]) + 0.2])
    plt.title('I-Chart', fontsize=30)
    plt.show()
    # draw MR chart
    plt.figure(figsize=(15, 7))
    plt.plot(x[1:], imr_list, color='blue', label='EWMA')
    plt.axhline(y=UCLmr, color='green', label='UCL', linestyle='--')
    plt.axhline(y=LCLmr, color='green', label='LCL', linestyle='--')
    plt.axhline(y=imr_avg, color='green', label='LCL', linestyle='--')
    check_points(imr_list, UCLmr, LCLmr, shift=1)
    plt.xlabel('Axe x', fontsize=16)
    plt.ylabel('Axe y', fontsize=16)
    plt.xlim([0.8, len(list_of_columns[0]) + 0.2])
    plt.title('MR-Chart', fontsize=30)
    plt.show()
