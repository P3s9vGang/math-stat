from tkinter.filedialog import askopenfilename
from emwa_chart import emwa_chart

# TODO - Цвета area

url = askopenfilename()
print(url)
emwa_chart(url)
