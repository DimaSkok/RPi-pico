import serial


port = "COM7"
baudrate = 115200

ser = serial.Serial(port, baudrate)

def read_memory(address):
    ser.write(f"read_mem {address}\n".encode()) 
    response = ser.readline().decode().strip()  
    print(response)

def led_on():
    ser.write("led_on\n".encode())
    response = ser.readline().decode().strip()
    print(response)

def led_off():
    ser.write("led_off\n".encode())
    response = ser.readline().decode().strip()
    print(response)

mem = " "

try:
    led_on()
    read_memory("0x20000000")  
    led_off()
    led_on()
    read_memory("0x20000004")
    led_off()
    while mem != "stop":
        mem = input("Введите адресс ")
        led_on()
        read_memory(mem)
        led_off()

except serial.SerialException as e:
    print(f"Serial port error: {e}")

finally:
    ser.close()