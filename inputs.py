import datetime
import re
import display
import sys
from database import *

database = DataBaseQueries()


def choice():
    try:
        choice1 = int(input(" Enter the choice : "))
        return choice1
    except ValueError:
        print(" invalid inputs ")
        choice()


def login_inputs():
    username = input("enter the username : ")
    password = input("enter the password : ")

    return username, password


def password_change_inputs():
    new_password = input("enter new password : ")
    old_password = input("enter old_password : ")

    return new_password, old_password


def space_update_inputs():
    two_wheleer = input("Enter two_wheleer space  : ")
    Car = input("Enter car sapce                  : ")
    SUV = input("Enter SUV space                  : ")
    Truck = input("Enter truck space              : ")

    return two_wheleer, Car, SUV, Truck


def cost_update_inputs():
    try:
        two_wheleer_cost = int(input("Enter two_wheleer space       : "))
        Car_cost = int(input("Enter car sapce                  : "))
        SUV_cost = int(input("Enter SUV space                  : "))
        Truck_cost = int(input("Enter truck space              : "))

        return two_wheleer_cost, Car_cost, SUV_cost, Truck_cost
    except ValueError:
        print("sorry invalid inputs :")
        cost_update_inputs()


def registration_inputs():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # username and password details
    user_name = input("enter the user name : ")
    pass_word = input("enter the password : ")
    pass_word2 = input("pls re_enter password for verification :")
    if pass_word == pass_word2:
        pass
    else:
        print("password not matched please enter again")
        pass_word2 = input("pls re_enter password for verification :")
        if pass_word == pass_word2:
            pass
        else:
            print("password not matched please enter again")
            sys.exit(0)

    return date, user_name, pass_word


def spacing_inputs():
    try:
        # getting the space available for parking
        two_wheeler_spacing = int(input("two_wheeler_spacing : "))
        car_spacing = int(input("car_spacing : "))
        SUV_spacing = int(input("SUV_spacing : "))
        Truck_spacing = int(input("Truck_spacing : "))
        return two_wheeler_spacing, car_spacing, SUV_spacing, Truck_spacing,
    except ValueError:
        print("please enter the valid details")
        spacing_inputs()


def cost_inputs():
    try:
        # getting the cost details for each vehicle type
        cost_two_wheleer = int(input("enter the cost of two_wheleer/day : "))
        cost_car = int(input("enter the cost of car/day : "))
        cost_SUV = int(input("enter the cost of SUV/day : "))
        cost_Truck = int(input("enter the cost of Truck/day : "))

        return cost_two_wheleer, cost_car, cost_SUV, cost_Truck
    except ValueError:
        print("please enter the valid details")
        cost_inputs()


def vehicle_entry_inputs():
    global ph_num, two_wheleer_spacing, Truck_spacing, SUV_spacing, car_spacing
    try:
        vehicle_type = int(input("vehicle type : "))

        if vehicle_type == 1:
            vehicle_type = "Two_wheeler"
        elif vehicle_type == 2:
            vehicle_type = "Car"
        elif vehicle_type == 3:
            vehicle_type = "SUV"
        elif vehicle_type == 4:
            vehicle_type = "Truck"
        else:
            print("sorry parking not available.")

        # fetching the spacing details from parking_space table
        count = database.parking_space()
        if vehicle_type == "Two_wheeler":
            two_wheleer_spacing = int(count[0])
        elif vehicle_type == "Car":
            car_spacing = int(count[1])
        elif vehicle_type == "SUV":
            SUV_spacing = int(count[2])
        elif vehicle_type == "Truck":
            Truck_spacing = int(count[3])

        # fetching the available space details from customers table based on vehicle IN
        data = database.space_availabe(vehicle_type)

        if vehicle_type == "Two_wheeler":
            space = two_wheleer_spacing - data[0]
            if space == 0:
                print(f"sorry parking full for {vehicle_type}")

            else:
                print(f"available parking space for {vehicle_type} :", space)

        elif vehicle_type == "Car":
            space = car_spacing - data[0]
            if space == 0:
                print(f"sorry parking full for {vehicle_type}")

            else:
                print(f"available parking space for {vehicle_type} :", space)
        elif vehicle_type == "SUV":
            space = SUV_spacing - data[0]
            if space == 0:
                print(f"sorry parking full for {vehicle_type}")

            else:
                print(f"available parking space for {vehicle_type} :", space)
        elif vehicle_type == "Truck":
            space = Truck_spacing - data[0]
            if space == 0:
                print(f"sorry parking full for {vehicle_type}")

            else:
                print(f"available parking space for {vehicle_type} :", space)

        # getting customer details
        name = input("Enter you name : ").title().strip()
        try:
            ph_num = int(input("Enter your ph_num : "))
            # validating ph_num
            regex = "^[6-9][0-9]{9}$"
            if re.match(regex, str(ph_num)):
                pass
            else:
                print("Invalid Phone_number")
                vehicle_entry_inputs()

        except ValueError:
            print("sorry invalid input")
        # validating vehicle number as per indian standards
        vehicle_num = input("Enter the vehicle_num : ").upper()
        regex = "^[A-Z]{2}[0-9]{2}[A-Z][0-9]{4}$"
        if re.match(regex, str(vehicle_num)):
            pass
        else:
            print("Invalid vehicle_num")
            vehicle_entry_inputs()

        data1 = database.vehicle_status(vehicle_num)
        if data1 is None:
            pass
        elif data1 == vehicle_num:
            print("sorry vehicle already IN :")
            print("please enter valid vehicle_num")
            vehicle_entry_inputs()

        IN_DATE = datetime.date.today().strftime("%Y-%m-%d")
        IN_TIME = datetime.datetime.now().time().strftime("%H:%M:%S")
        status = "IN"

        return IN_DATE, IN_TIME, name, ph_num, vehicle_num, vehicle_type, status
    except (ValueError, NameError, None):
        print("sorry something went wrong..")
        vehicle_entry_inputs()


def vehicle_out_inputs():
    ph_num = input("enter your ph_num : ")
    vehicle_num = input("enter the vehicle number : ").upper()
    OUT_DATE = datetime.date.today().strftime("%Y-%m-%d")
    OUT_TIME = datetime.datetime.now().time().strftime("%H:%M:%S")

    return OUT_DATE, OUT_TIME, ph_num, vehicle_num


def search_user_inputs():
    global ph_num
    try:
        ph_num = int(input("enter your ph_num : "))
    except ValueError:
        print("please enter the valid input ")
        search_user_inputs()
    vehicle_num = input("enter the vehicle number : ").upper()

    details = database.user_details(ph_num=ph_num, vehicle_num=vehicle_num)

    if details[6] is None:
        if details[8] is None:
            if details[9] is None:
                details[6], details[8], details[9] = "Null", "Null", "Null"

    if details is None:
        print("sorry no user....")
    else:
        display.user_details_display()

        print("| {:10} | {:10} | {:15} | {:10} | {:11} | {:11} | {:11} | {:11} | {:15} |{:15} |".format(
            details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7],
            details[8],
            details[9]))


def daily_input():
    try:
        year = int(input("enter the year YYYY : "))
        month = int(input("enter the month  mm  : "))
        date = int(input("enter the date  dd : "))
        date = datetime.date(year, month, date)

        return date
    except ValueError:
        print("sorry invalid input ")
        daily_input()


def monthly_input():
    month = input("enter the month as  mm  : ")
    year = input("enter the year as YYYY  : ")
    return month, year


def yearly_input():
    year = input("enter the year as YYYY  : ")
    return year
