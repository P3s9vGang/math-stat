from tkinter.filedialog import askopenfilename
from emwa_chart import emwa_chart
from memwa_chart import memwa_chart
from xr_chart import x_r_chart
from xs_chart import x_s_chart
from imr_chart import x_mr_chart
from cusum_chart import cusum_chart

url = askopenfilename()
cusum_chart(url)
print(url)
