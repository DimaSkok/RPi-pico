import serial
import time

PORT = 'COM7'  
BAUDRATE = 115200
t = 30

with open('data.csv', 'w', newline='') as f:
    pass

def writer (name1, name2, name3, t):
    with open ('data.csv', 'a') as seo:
        seo.write(str(name1) + ';' + str(name2) + ';' + str(name3) + ';' + str(t)[0:5] + '\n')
        
        seo.close()
    return


try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    print(f"Подключено к {PORT}")

    tim_s = time.time()
    tim_e = tim_s

    while ((tim_e - tim_s) <= t):
        response1 = ser.readline().decode().strip() 
        response2 = ser.readline().decode().strip()
        response3 = ser.readline().decode().strip() 
        writer(response1, response2, response3, (tim_e - tim_s))
        print(response1, response2, response3)
        tim_e = time.time()
    



except serial.SerialException as e:
    print(f"Ошибка подключения к COM-порту: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Соединение закрыто.")
