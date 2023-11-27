from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def x_s_chart(url):
    table = pd.read_excel(f'{url}')
    # how many columns in table
    list_of_columns = []
    for i in range(len(table.columns)):
        list_of_columns.append(table.values[:, i])
    x = list(range(1, len(list_of_columns[0]) + 1))
    list_of_columns = np.array(list_of_columns).transpose()
    lamda = 0.2
    n = len(list_of_columns[0])
    L = 1
    x_avg = []
    s_avg = []
    x_r_points = []
    for i in list_of_columns:
        cur_list = []
        for cur in i:
            cur_list.append(cur)
        x_avg.append(sum(cur_list) / len(cur_list))
        sm = 0
        for j in range(len(cur_list)):
            sm += (cur_list[j] - x_avg[-1]) ** 2
        s_avg.append(sqrt(sm / (len(cur_list) - 1)))
    CL = sum(x_avg) / len(x_avg)
    S = sum(s_avg) / len(s_avg)
    # constants
    A3 = [2.6587, 1.9544, 1.6281, 1.4273, 1.2871, 1.1822, 1.0994, 1.0325, 0.9776, 0.9317, 0.8923, 0.8577, 0.8264, 0.7979, 0.7717, 0.7475, 0.7251, 0.7041, 0.6845, 0.6661, 0.6487, 0.6323, 0.6167, 0.6019, 0.5877, 0.5742, 0.5612, 0.5487, 0.5367, 0.5251, 0.5139, 0.5031, 0.4926, 0.4824, 0.4725, 0.4629, 0.4535, 0.4444, 0.4355, 0.4268, 0.4184, 0.4101, 0.402, 0.3941, 0.3863, 0.3787, 0.3712, 0.3639, 0.3567, 0.3496, 0.3426, 0.3357, 0.3289, 0.3222, 0.3156, 0.3091, 0.3026, 0.2963, 0.29, 0.2838, 0.2777, 0.2716, 0.2656, 0.2597, 0.2538, 0.248, 0.2422, 0.2365, 0.2308, 0.2252, 0.2196, 0.2141, 0.2086, 0.2031, 0.1977, 0.1923, 0.187, 0.1817, 0.1764, 0.1712, 0.166, 0.1608, 0.1557, 0.1506, 0.1455, 0.1405, 0.1355, 0.1305, 0.1256, 0.1207, 0.1158, 0.111, 0.1062, 0.1014, 0.0967, 0.092, 0.0873, 0.0827]
    B3 = [0.0, 0.0, 0.0, 0.0, 0.030, 0.118, 0.185, 0.239, 0.284, 0.321, 0.354, 0.382, 0.406, 0.428, 0.448, 0.466, 0.482, 0.497, 0.510, 0.523, 0.534, 0.545, 0.555, 0.565, 0.574, 0.583, 0.591, 0.599, 0.606, 0.613, 0.620, 0.626, 0.632, 0.638, 0.643, 0.649, 0.654, 0.659, 0.664, 0.669, 0.674, 0.678, 0.683, 0.687, 0.691, 0.695, 0.699, 0.703, 0.707, 0.710, 0.714, 0.717, 0.721, 0.724, 0.727, 0.730, 0.733, 0.736, 0.739, 0.742, 0.745, 0.747, 0.750, 0.752, 0.755, 0.757, 0.760, 0.762, 0.764, 0.767, 0.769, 0.771, 0.773, 0.775, 0.777, 0.779, 0.781, 0.783, 0.785, 0.787, 0.789, 0.791, 0.793, 0.794, 0.796, 0.798, 0.799, 0.801, 0.802, 0.804, 0.805, 0.807, 0.808, 0.809, 0.811, 0.812, 0.813, 0.815, 0.816, 0.817, 0.818, 0.819, 0.820, 0.821, 0.822, 0.823, 0.824, 0.825, 0.826, 0.827, 0.828, 0.829, 0.830, 0.831, 0.832, 0.833, 0.834, 0.835, 0.836, 0.837, 0.838, 0.839, 0.840, 0.841, 0.842, 0.843, 0.844, 0.845, 0.846, 0.847, 0.848, 0.849, 0.850, 0.851, 0.852, 0.853, 0.854, 0.855, 0.856, 0.857, 0.858, 0.859, 0.860, 0.861, 0.862, 0.863, 0.864, 0.865, 0.866, 0.867, 0.868, 0.869, 0.870, 0.871, 0.872, 0.873, 0.874, 0.875, 0.876, 0.877, 0.878, 0.879, 0.880, 0.881, 0.882, 0.883, 0.884, 0.885, 0.886, 0.887, 0.888, 0.889, 0.890, 0.891, 0.892, 0.893, 0.894, 0.895, 0.896, 0.897, 0.898, 0.899, 0.900, 0.901, 0.902, 0.903, 0.904, 0.905, 0.906, 0.907, 0.908, 0.909, 0.910, 0.911, 0.912, 0.913, 0.914, 0.915, 0.916, 0.917, 0.918]
    B4 = [3.267, 2.568, 2.266, 2.089, 1.97, 1.882, 1.815, 1.761, 1.716, 1.679, 1.646, 1.618, 1.594, 1.572, 1.552, 1.534, 1.518, 1.503, 1.49, 1.477, 1.466, 1.455, 1.445, 1.435, 1.426, 1.418, 1.41, 1.402, 1.394, 1.388, 1.381, 1.375, 1.369, 1.363, 1.358, 1.352, 1.347, 1.342, 1.337, 1.333, 1.328, 1.324, 1.32, 1.316, 1.312, 1.308, 1.304, 1.301, 1.297, 1.294, 1.291, 1.287, 1.284, 1.281, 1.278, 1.275, 1.272, 1.269, 1.266, 1.264, 1.261, 1.258, 1.256, 1.253, 1.251, 1.248, 1.246, 1.244, 1.241, 1.239, 1.237, 1.235, 1.233, 1.231, 1.229, 1.227, 1.225, 1.223, 1.221, 1.219, 1.217, 1.215, 1.214, 1.212, 1.21, 1.208, 1.207, 1.205, 1.203, 1.202, 1.2, 1.198, 1.197, 1.195, 1.194, 1.192, 1.191, 1.189, 1.188, 1.187, 1.185, 1.184, 1.182, 1.181, 1.18, 1.178, 1.177, 1.176, 1.174, 1.173, 1.172, 1.171, 1.169, 1.168, 1.167, 1.166, 1.164, 1.163, 1.162, 1.161, 1.16, 1.159, 1.158, 1.157, 1.155, 1.154, 1.153, 1.152, 1.151, 1.15, 1.149, 1.148, 1.147, 1.146, 1.145, 1.144, 1.143, 1.142, 1.141, 1.14, 1.139, 1.138, 1.137, 1.136, 1.135, 1.134, 1.133, 1.132, 1.131, 1.13, 1.129, 1.128, 1.127, 1.126, 1.125, 1.124, 1.123, 1.122, 1.121, 1.12, 1.119, 1.118, 1.117, 1.116, 1.115, 1.114, 1.113, 1.112, 1.111, 1.11, 1.109, 1.108, 1.107, 1.106, 1.105, 1.104, 1.103, 1.102, 1.101, 1.1, 1.099, 1.098, 1.097, 1.096, 1.095, 1.094, 1.093, 1.092, 1.091, 1.09, 1.089, 1.088, 1.087, 1.086, 1.085, 1.084, 1.083, 1.082, 1.081, 1.08]
    UCLx = CL + A3[n - 2] * S
    LCLx = CL - A3[n - 2] * S
    UCLs = B4[n - 2] * S
    LCLs = B3[n - 2] * S
    def check_points(x_avg, UCLx, LCLx):
        for i in range(len(x_avg)):
            if x_avg[i] >= UCLx or x_avg[i] <= LCLx:
                plt.scatter(i + 1, x_avg[i], s=300, c='red', marker='X')
            else:
                plt.scatter(i + 1, x_avg[i], s=120, c='blue', marker='o')
    plt.figure(figsize=(15, 7))
    plt.plot(x, x_avg, color='blue', label='EWMA')
    plt.axhline(y=UCLx, color='green', label='UCL', linestyle='--')
    plt.axhline(y=LCLx, color='green', label='LCL', linestyle='--')
    plt.axhline(y=CL, color='green', label='LCL', linestyle='--')
    check_points(x_avg, UCLx, LCLx)
    plt.xlabel('Axe x', fontsize=16)
    plt.ylabel('Axe y', fontsize=16)
    plt.xlim([0.8, len(x_avg) + 0.2])
    plt.title('X-bar Chart', fontsize=30)
    plt.show()
    # draw R chart
    plt.figure(figsize=(15, 7))
    plt.plot(x, s_avg, color='blue', label='EWMA')
    plt.axhline(y=UCLs, color='green', label='UCL', linestyle='--')
    plt.axhline(y=LCLs, color='green', label='LCL', linestyle='--')
    plt.axhline(y=S, color='green', label='LCL', linestyle='--')
    check_points(s_avg, UCLs, LCLs)
    plt.xlabel('Axe x', fontsize=16)
    plt.ylabel('Axe y', fontsize=16)
    plt.xlim([0.8, len(x_avg) + 0.2])
    plt.title('S Chart', fontsize=30)
    plt.show()