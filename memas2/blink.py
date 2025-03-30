import serial
import time

port = "COM7"
baudrate = 115200

ser = serial.Serial(port, baudrate)

def send_command(command):
    ser.write(f"{command}\n".encode())
    response = ser.readline().decode().strip()
    if response == "OK":
        return True  
    else:
        print(f"Error: {response}")
        return False 

def read_memory(address):
    ser.write(f"read_mem {address}\n".encode())
    response = ser.readline().decode().strip()  
    ack = ser.readline().decode().strip()
    if ack == "OK":
        print(response)
        return True
    else:
        print(f"Error: {response}")
        return False

def led_on():
    return send_command("led_on")

def led_off():
    return send_command("led_off")

mem = " "

try:
    read_memory("0x20000000")
    read_memory("0x20000004")

    while mem != "stop":
        mem = input("Введите адресс ")
        read_memory(mem)


except serial.SerialException as e:
    print(f"Serial port error: {e}")

finally:
    ser.close()