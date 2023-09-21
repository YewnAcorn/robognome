# import RPi.GPIO as GPIO
import time
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(22, GPIO.OUT)

def water_log():
    statusA = get_status_A()
    statusB = get_status_B()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('water.log', 'a') as f:
        f.write(f"{current_time} | A {statusA} | B {statusB} ")


def read_durationB():
    with open('durationB.txt', 'r') as f:
        duration = int(f.read().strip())
    return duration
        
def change_status_B(switch):
    if switch == "on" || switch == "off":
        with open('statusB', 'w') as f:
            f.write(str(switch))
    else:
        print(">>>Invalid input {switch} please enter on or off<<<")

def get_status_A():
    with open('statusA', 'r') as f:
        status = f.read().strip()
    print(status)
    return status

def get_status_B():
    with open('statusB', 'r') as f:
        status = f.read().strip()
    print(status)
    return status


duration = read_durationB()

print("Status B = on")
change_status_B("on")
water_log()
print("watering...")
# GPIO.output(22, GPIO.HIGH) # turn on the pin (to start the watering)
print(f"for {duration} seconds")
time.sleep(duration)
print("status B = off")
change_status_B("off")
water_log()
print("complete")
# GPIO.output(22, GPIO.LOW) # turn off the pin (watering complete)
print("valve closed")


