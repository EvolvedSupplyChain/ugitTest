import machine
import time

def log_data():
    print("Attempt number 1")
    led = machine.Pin(10, machine.Pin.OUT)
        
    while True:
        try:
            led.on()
        except Exception as error:
            print(error)
            
        print("5555")
        time.sleep(1)
        led.off()
    return
