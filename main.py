from tkinter.filedialog import askopenfilename
from emwa import emwa
from memwa import memwa
from xbar_rbar import xbar_rbar
from xbar_sbar import xbar_sbar
from imrx import imrx
from cusum import cusum

path_file = askopenfilename()

print("1. emwa (len subgroup = 1) \n2. memwa\n3. xbar_rbar (len subgroup 2 to 8)\n4. xbar_sbar (len subgroup from 9)\n5. imrx (len subgroup = 1)\n6. cusum (len subgroup = 1)")
choose_chart = int(input())

match choose_chart:
    case 1:
        emwa(path_file)
    case 2:
        memwa(path_file)
    case 3:
        xbar_rbar(path_file)
    case 4:
        xbar_sbar(path_file)
    case 5:
        imrx(path_file)
    case 6:
        cusum(path_file)
    case _:
        print("error")
