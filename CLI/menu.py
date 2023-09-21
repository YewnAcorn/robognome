from datetime import datetime
import os
# import RPi.GPIO as GPIO
import time
import plant_art
import random


# GPIO.setmode(GPIO.BCM)
# GPIO.setup(pi_pin, GPIO.OUT)

def welcome_screen():
    print_random_art()
    print("Welcome to")
    plant_art.print_FarmBrain()

def print_random_art():
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

def show_menu():
    print("----------------------")
    print("  Irrigation Control")
    print("----------------------")
    print("Menu: ")
    print("[1] Turn Water On [1]")
    print("[2] Turn Water Off [2]")
    print()
    print("[3] Change Duration [3]")
    print()
    print("[4] Add New Watering Schedule [4]")
    print("[5] Delete A Watering Schedule [5]")
    print()
    print("[6] View logs [6]")
    print("[7] Show Status [7]")
    print()
    print("[9] Exit [9]")
    print("[0] About [0]")
    print()
    choice = input("Enter your choice: ")
    print(f"[{choice}]")
    return choice

def change_status_A(switch):
    if switch == "on" or switch == "off":
        with open('statusA', 'w') as f:
            f.write(str(switch))
    else:
        print(">>>Invalid input {switch} please enter on or off<<<")

def change_status_B(switch):
    if switch == "on" or switch == "off":
        with open('statusB', 'w') as f:
            f.write(str(switch))
    else:
        print(">>>Invalid input {switch} please enter on or off<<<")

def get_status_A():
    with open('statusA', 'r') as f:
        status = f.read().strip()
    print(f"A status: {status}")
    return status

def get_status_B():
    with open('statusB', 'r') as f:
        status = f.read().strip()
    print(f"B status: {status}")
    return status

def turn_water_on(pi_pin):
    print("Turning water on")
    t = time.localtime()
    time_on = time.strftime("%H:%M:%S", t)
    print(f"watering @ {time_on}")
 #   GPIO.output(pi_pin, GPIO.HIGH)
    if pi_pin == 5:
        change_status_A("on")
    elif pi_pin == 22:
        change_status_B("on")
    water_log()

def turn_water_off(pi_pin):
    print("Turning water off")
    t = time.localtime()
    time_off = time.strftime("%H:%M:%S", t)
    print(f"valve closed @ {time_off}")
 #   GPIO.output(pi_pin, GPIO.LOW)
    if pi_pin == 5:
        change_status_A("off")
    elif pi_pin == 22:
        change_status_B("off")
    water_log()

def write_duration1(duration):
    with open('durationA.txt', 'w') as f:
        f.write(str(duration))

def write_duration2(duration):
    with open('durationB.txt', 'w') as f:
        f.write(str(duration))

def change_duration1():
    new_duration = input("Enter time in seconds: ")
    if new_duration.isdigit():
        write_duration1(new_duration)
        print(f"Valve A will water for {new_duration} seconds")
    else:
        print(">>>Invalid input. Value must be an integer<<<")
        time.sleep(2)

def change_duration2():
    new_duration = input("Enter time in seconds: ")
    if new_duration.isdigit():
        write_duration2(new_duration)
        print(f"Valve B will water for {new_duration} seconds")
    else:
        print(">>>Invalid input. Value must be an integer<<<")
        time.sleep(2)


def add_watering_schedule_A():
    hour = input("Enter the hour for the watering schedule (0-23): ")
    minute = input("Enter the minute for the watering schedule (0-59): ")
    print(f"Adding new watering schedule at {hour}:{minute}")
    # cron job implementation: 
    os.system(f"(crontab -l; echo '{minute} {hour} * * * /home/pi/robognome/CLI/powerto5.py) | crontab -")

def add_watering_schedule_B():
    hour = input("Enter the hour for the watering schedule (0-23): ")
    minute = input("Enter the minute for the watering schedule (0-59): ")
    print(f"Adding new watering schedule at {hour}:{minute}")
    # cron job implementation: 
    os.system(f"(crontab -l; echo '{minute} {hour} * * * /home/pi/robognome/CLI/powerto22.py) | crontab -")


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

def water_log():
    statusA = get_status_A()
    statusB = get_status_B()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('water.log', 'a') as f:
        f.write(f"{current_time} | A {statusA} | B {statusB} ")


def print_logs():
    with open('water.log', 'r') as f:
        for line in f:
            print(line.strip())


if __name__ == "__main__":
    welcome_screen()

    while True:
        choice = show_menu()
        # Menu
        # [1] Turn water on
        if choice == "1":
            valve_choice = input("A or B? ")
            if valve_choice == "A":
                print("Turning on water on A")
                turn_water_on(5)
                time.sleep(2)
            elif valve_choice == "B":
                print("Turning water on B")
                turn_water_on(22)
            else:
                print(f">>> Invalid input ({valve_choice} please enter A or B <<<")
                time.sleep(2)
        # [2] Turn water off
        elif choice == "2":
            valve_choice = input("A or B? ")
            if valve_choice == "A":
                print("Turning off water on A")
                turn_water_off(5)
                time.sleep(2)
            elif valve_choice == "B":
                print("Turning water off B")
                turn_water_on(22)
                time.sleep(2)
            else:
                print(f">>> Invalid input ({valve_choice} please enter A or B <<<")
                time.sleep(2)
        # [3] Change Duration
        elif choice == "3":
            valve_choice = input("A or B? ")
            if valve_choice == "A":
                print("Changing duration on valve A")
                change_duration1()
                time.sleep(2)
            elif valve_choice == "B":
                print("Changing duration on valve B")
                change_duration2()
                time.sleep(2)
        # [4] Add New Watering Schedule
        elif choice == "4":
            valve_choice = input("A or B?")
            if valve_choice == "A":
                print("Changing schedule on A")
                add_watering_schedule_A()
                time.sleep(2)
            elif valve_choice == "B":
                print("Changing schedule on B")
                add_watering_schedule_B()
                time.sleep(2)
        # [5] Delete A Watering Schedule
        elif choice == "5":
            print("Printing deletion instructions")
            delete_last_watering_schedule()
            time.sleep(6)
            print()
            print(">> Main menu:")
            time.sleep(1)
        # [6] View logs
        elif choice == "6":
            print("Printing log data")
            print_logs()
        # [7] Show status
        elif choice == "7":
            print("Showing status")
            get_status_A()
            get_status_B()
            time.sleep(2)
        # [9] Exit
        elif choice == "9":
            print("Exiting...")
            break
        # [0] About
        elif choice == "0":
            print()
            print("About: ")
            print("FarmBrain was made in python")
            print("by Carter Gunderson in 2023") 
            print("for Sovereign Starts Seedling Company")
            time.sleep(3)
            print("It's gonna grow!!")
            time.sleep(2)
            print("         3")
            time.sleep(1)
            print("    2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print_random_art()
        else:
            print(">>> Invalid choice. Please try again <<<")
            time.sleep(1)

