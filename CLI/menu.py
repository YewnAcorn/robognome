from datetime import datetime
import os
# import RPi.GPIO as GPIO
import time
import plant_art
import random
from typing import Literal, Union, cast

ValveId = Literal["A", "B"]
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

def change_status(switch: Literal["on", "off"], valve_id: ValveId):
    if switch == "on" or switch == "off":
        with open(f"status{valve_id}", 'w') as f:
            f.write(str(switch))
    else:
        print(f">>>Invalid input {switch} please enter on or off<<<")

def get_status(valve_id: ValveId):
    with open(f"status{valve_id}", 'r') as f:
        status = f.read().strip()
    print(f"{valve_id} status: {status}")

    return status

def turn_water_on(valve_id: ValveId):
    print("Turning water on")
    t = time.localtime()
    time_on = time.strftime("%H:%M:%S", t)
    print(f"watering @ {time_on}")
 #   GPIO.output(pi_pin, GPIO.HIGH)
    change_status("on", valve_id)
    water_log()

def turn_water_off(valve_id: ValveId):
    print("Turning water off")
    t = time.localtime()
    time_off = time.strftime("%H:%M:%S", t)
    print(f"valve closed @ {time_off}")
 #   GPIO.output(pi_pin, GPIO.LOW)
    change_status("off", valve_id)
    water_log()

def write_duration(duration, valve_id: ValveId):
    with open(f'duration{valve_id}.txt', 'w') as f:
        f.write(str(duration))

def change_duration(valve_id: ValveId):
    new_duration = input("Enter time in seconds: ")
    if new_duration.isdigit():
        write_duration(new_duration, valve_id)
        print(f"Valve {valve_id} will water for {new_duration} seconds")
    else:
        print(">>>Invalid input. Value must be an integer<<<")
        time.sleep(2)

def add_watering_schedule(valve_id: ValveId):
    hour = input("Enter the hour for the watering schedule (0-23): ")
    minute = input("Enter the minute for the watering schedule (0-59): ")
    print(f"Adding new watering schedule at {hour}:{minute}")
    pi_pin = get_pin(valve_id)
    # cron job implementation: 
    os.system(f"(crontab -l; echo '{minute} {hour} * * * /home/pi/robognome/CLI/powerto{pi_pin}.py') | crontab -")

def get_pin(valve_id: ValveId):
    return 5 if valve_id == "A" else 22

def get_valve_ids() -> list[ValveId]:
    return ["A", "B"]

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
    valve_statuses = [f"{valve_id} {get_status(valve_id)}" for valve_id in get_valve_ids()]
    delimited_statuses = " | ".join(valve_statuses)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('water.log', 'a') as f:
        f.write(f"{current_time} | {delimited_statuses} \n")


def print_logs():
    with open('water.log', 'r') as f:
        for line in f:
            print(line.strip())

def request_valve_choice() -> Union[ValveId, Literal[False]]:
    valve_choice = input("A or B? ")
    if not valve_choice in ["A", "B"]:
        print(f">>> Invalid input ({valve_choice} please enter A or B <<<")
        time.sleep(2)
        return False
    return cast(ValveId, valve_choice)

if __name__ == "__main__":
    welcome_screen()

    while True:
        choice = show_menu()
        # Menu
        # [1] Turn water on
        if choice == "1":
            valve_choice = request_valve_choice()
            if not valve_choice:
                continue
            print(f"Turning on water on {valve_choice}")
            turn_water_on(valve_choice)
            time.sleep(2)
        # [2] Turn water off
        elif choice == "2":
            valve_choice = request_valve_choice()
            if not valve_choice:
                continue
            print(f"Turning off water on {valve_choice}")
            turn_water_off(valve_choice)
            time.sleep(2)
        # [3] Change Duration
        elif choice == "3":
            valve_choice = request_valve_choice()
            if not valve_choice:
                continue
            print(f"Changing duration on valve {valve_choice}")
            change_duration(valve_choice)
            time.sleep(2)
        # [4] Add New Watering Schedule
        elif choice == "4":
            valve_choice = request_valve_choice()
            if not valve_choice:
                continue
            print(f"Changing schedule on {valve_choice}")
            add_watering_schedule(valve_choice)
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
            for valve_id in get_valve_ids():
                get_status(valve_id)
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

