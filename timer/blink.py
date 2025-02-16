import serial
import time

PORT = 'COM7'  
BAUDRATE = 115200
# ввожу mem + адресс и получаю значение с этого адреса

try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    print(f"Подключено к {PORT}")

    while True:
        t = input("Введите количество секунд ")

        ser.write(('e' + '\n').encode('utf-8'))
        time.sleep(float(t))
        ser.write(('d' + '\n').encode('utf-8'))


except serial.SerialException as e:
    print(f"Ошибка подключения к COM-порту: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Соединение закрыто.")

