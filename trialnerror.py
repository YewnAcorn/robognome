#This is a script for using this pi HAT hardware 
#That uses a GPIO pin to turn on a relay
#But I couldnt find documentation on what pins
#It uses so this is a script that does trial and error
#and I just ran this script and watched the relay
#In this case on the 2 relay hat for the pi Zero
# it was pins 5 and 22
import RPi.GPIO as GPIO
import time

# Set the numbering scheme
GPIO.setmode(GPIO.BCM)

# List of GPIO pins you want to test (Modify this list)
pins_to_test = [2,3,4,17,27,22,10,9,11,0,5,6,13,19,26,14,15,18,23,24,25,8,7,1,12,16,20,21]

# Setup pins as outputs and set to LOW initially
for pin in pins_to_test:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        for pin in pins_to_test:
            print(f"Activating Pin {pin}")
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(2)
            
            print(f"Deactivating Pin {pin}")
            GPIO.output(pin, GPIO.LOW)
            time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Cleanup GPIO settings
    GPIO.cleanup()

