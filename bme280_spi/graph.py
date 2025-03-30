# & C:/Users/Dimasik/AppData/Local/Programs/Python/Python313/python.exe -m pip install pyserial

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

with open('data.csv', 'r') as FtoP:
    data = FtoP.read().split()
    FtoP.close()

time = [float(i.split(';')[-1]) for i in data]
data_hea = [float(i.split(';')[0]) for i in data]
data_pre = [float(i.split(';')[1]) for i in data]
data_tem = [float(i.split(';')[2]) for i in data]

# print(time, data_hea, data_pre, data_tem)


t =  int(float(time[-1]) // 1)
T = t / len(time)
data_t = []
for i in range(1, len(time) + 1):
    data_t.append(t * i / len(time))


fig, ax = plt.subplots(3, 1, figsize=(8, 10))  # Укажем количество подграфиков и размер

# График влажности
ax[0].plot(data_t, data_hea, color='red')
for i in range(0, len(data_hea), 5):
    ax[0].scatter(data_t[i], data_hea[i], marker='.', color='red')
ax[0].set_title('График зав-ти влажности от времени', loc='center')
ax[0].grid(True, which='both', color='grey')  # сетка
ax[0].yaxis.set_major_locator(MultipleLocator(10))  # Увеличиваем шаг
ax[0].yaxis.set_minor_locator(MultipleLocator(2))
ax[0].xaxis.set_major_locator(MultipleLocator(1)) # Увеличиваем шаг
ax[0].xaxis.set_minor_locator(MultipleLocator(1))


# График давления
ax[1].plot(data_t, data_pre, color='red')
for i in range(0, len(data_pre), 5):
    ax[1].scatter(data_t[i], data_pre[i], marker='.', color='red')
ax[1].set_title('График зав-ти давления от времени', loc='center')
ax[1].grid(True, which='both', color='grey')  # сетка
ax[1].yaxis.set_major_locator(MultipleLocator(20))  # Увеличиваем шаг
ax[1].yaxis.set_minor_locator(MultipleLocator(5))
ax[1].xaxis.set_major_locator(MultipleLocator(1)) # Увеличиваем шаг
ax[1].xaxis.set_minor_locator(MultipleLocator(1))

# График температуры
ax[2].plot(data_t, data_tem, color='red')
for i in range(0, len(data_tem), 5):
    ax[2].scatter(data_t[i], data_tem[i], marker='.', color='red')
ax[2].set_title('График зав-ти температуры от времени', loc='center')
ax[2].grid(True, which='both', color='grey')  # сетка
ax[2].yaxis.set_major_locator(MultipleLocator(1))
ax[2].yaxis.set_minor_locator(MultipleLocator(0.2))
ax[2].xaxis.set_major_locator(MultipleLocator(1)) # Увеличиваем шаг
ax[2].xaxis.set_minor_locator(MultipleLocator(1))

plt.tight_layout() # для правильного отображения графиков
#plt.text(-0.42, 2.75, '^')
#plt.text(-0.3, 2.74, 'V,В', color='blue')
#plt.text(8.9, 0.08, '>')
#plt.text(8.9, 0.02, 't,с', color='blue')
# ax.legend()
# fig.savefig('graphic.svg')
plt.show()