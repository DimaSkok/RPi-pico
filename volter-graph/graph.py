# & C:/Users/Dimasik/AppData/Local/Programs/Python/Python313/python.exe -m pip install pyserial

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

with open('D:\git\RPi pico\hello_adc\data_con.csv', 'r') as FtoP:
    data = FtoP.read().split()
    FtoP.close()

time = data[1::2]
data_r = [float(i) for i in data[0::2]]
# print(data_r)
t =  int(float(time[-1]) // 1)
T = t / len(time)
data_t = []
for i in range(1, len(time) + 1):
    data_t.append(t * i / len(time))


fig, ax = plt.subplots(figsize = (16, 9), dpi = 100)
ax.plot(data_t, data_r, color='red', label='V(t)')
for i in range(0, len(data_r), 5):
    ax.scatter(data_t[i], data_r[i], marker='.', color='red')
ax.set_title('График зав-ти напряжения от времени', loc='center')
ax.grid(True, which='both', color='grey')    # сетка
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
#plt.text(-0.42, 2.75, '^')
#plt.text(-0.3, 2.74, 'V,В', color='blue')
#plt.text(8.9, 0.08, '>')
#plt.text(8.9, 0.02, 't,с', color='blue')
ax.legend()
fig.savefig('graphic_con.svg')
plt.show()