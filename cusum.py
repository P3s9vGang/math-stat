import pandas as pd
import drow_chart


def cusum(path_file):
    table_excel = pd.read_excel(f'{path_file}')
    data_list = []

    for i in range(len(table_excel.columns)):
        data_list.append(table_excel.values[:, i])
    imr_list = []  # MR = |x(i+1) - xi|

    for i in range(1, len(data_list[0])):
        imr_list.append(abs(data_list[0][i - 1] - data_list[0][i]))

    CL = sum(data_list[0]) / len(data_list[0])
    imr_avg = sum(imr_list) / len(imr_list)
    d3 = 1.128  # const for i-mr chart
    sigma = imr_avg / d3

    w = 0.008  # TODO - Choose the critical level parameter
    u = CL  # TODO - Choose the target value
    UCL = 4 * sigma # control limit for i-mr
    LCL = -4 * sigma
    uc_list, lc_list = [], []

    for i in range(0, len(data_list[0])):
        if i == 0:
            uc_list.append(max(0, 0 + data_list[0][i] - w - u))
            lc_list.append(min(0, 0 + data_list[0][i] + w - u))
            continue
        uc_list.append(max(0, uc_list[i - 1] + data_list[0][i] - w - u))
        lc_list.append(min(0, lc_list[i - 1] + data_list[0][i] + w - u))

    drow_chart.draw_chart(points=uc_list, ucl=[UCL], lcl=[LCL], CL=0, name='CUSUM Chart', count=2)
    drow_chart.draw_chart(points=lc_list, ucl=[UCL], lcl=[LCL], CL=0, name='CUSUM Chart', count=2)
