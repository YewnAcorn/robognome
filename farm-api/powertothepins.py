import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT) # pin 11 on the board


rain = True

r = open('/home/pi/Gardenbot/dsaGreenhouseProjectFall2022/testing-api/isItRain.txt', 'r')
code = r.readline()

if (code == 'rain\n'):
    rain = True
    print("rain = True")
if(code == 'nope\n'):
    rain = False
    print("rain = False")
else:
    print("input error")
    print(code)
    for letter in code:
        print(ord(letter))
    print("string nope")
    for letter in "nope":
        print(ord(letter))

# if it didn't rain
if(rain != True):
    print("no rain, watering...")
    GPIO.output(15, GPIO.HIGH) # turn on the pin (to start the watering)
    print("for 300 seconds")
    time.sleep(300) # water for 100 seconds
    print("complete")
    GPIO.output(15, GPIO.LOW)
    print("valve closed")


