import os
# import RPi.GPIO as GPIO
import time
import plant_art
import random

pi_pin = 21

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(pi_pin, GPIO.OUT)

def welcome_screen():
    random.seed(time.time())
    options = [1,2,3,4,5,6]
    msg = random.choice(options)
    lookup = { 1:plant_art.print_bigTree,
               2:plant_art.print_halfTree,
               3:plant_art.print_miseltoe,
               4:plant_art.print_weed,
               5:plant_art.print_heartTree,
               6:plant_art.print_twoPines }
    welcome_msg = lookup.get(msg)
    welcome_msg()
    print("Welcome to")
    plant_art.print_FarmBrain()

def show_menu():
    print("----------------------")
    print("  Irrigation Control")
    print("----------------------")
    print("Menu: ")
    print("1. Turn Water On")
    print("2. Turn Water Off")
    print("3. Add New Watering Schedule")
    print("4. Delete A Watering Schedule")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def turn_water_on():
    print("Turning water on")
    t = time.localtime()
    time_on = time.strftime("%H:%M:%S", t)
    print(f"watering @ {time_on}")
  #  GPIO.output(pi_pin, GPIO.HIGH)

def turn_water_off():
    print("Turning water off")
    t = time.localtime()
    time_off = time.strftime("%H:%M:%S", t)
    print(f"valve closed @ {time_off}")
   # GPIO.output(pi_pin, GPIO.LOW)

def add_watering_schedule():
    hour = input("Enter the hour for the watering schedule (0-23): ")
    minute = input("Enter the minute for the watering schedule (0-59): ")
    print(f"Adding new watering schedule at {hour}:{minute}")
    # cron job implementation: 
    os.system(f"(crontab -l; echo '{minute} {hour} * * * /home/pi/Gardenbot/dsaGreenhouseProjectFall2022/testing-api/cronscript.sh') | crontab -")



def delete_last_watering_schedule():
    print()
    print("-------------------------")
    print(">>DELETION INSTRUCTIONS<<")
    print("-------------------------")
    print()
    print("> To delete a scheduled watering time:")
    print("> exit this program ")
    print("> in the command line:")
    print("> crontab -e")
    print("> displays the cron tables in editor mode")
    print("> find the line that contains the schedule you want to delete")
    print("> delete the line ")
    print("> save and exit")
    print()
    print("************^^^************")
if __name__ == "__main__":
    welcome_screen()

    while True:
        choice = show_menu()
        
        if choice == "1":
            turn_water_on()
        elif choice == "2":
            turn_water_off()
        elif choice == "3":
            add_watering_schedule()
        elif choice == "4":
            delete_last_watering_schedule()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

