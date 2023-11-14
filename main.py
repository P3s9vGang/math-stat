from tkinter.filedialog import askopenfilename
from emwa_chart import emwa_chart
from memwa_chart import memwa_chart

# TODO - Цвета area

url = askopenfilename()
print(url)
memwa_chart(url)
