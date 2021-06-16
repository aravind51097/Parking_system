from pathlib import Path
import sys
import os

DATABASE = Path("parking_system.db")


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def user_registration():
        user_input = inputs.registration_inputs()
        database.end_user_details(date=user_input[0], username=user_input[1], password=user_input[2])
        os.system("cls")

    def log_in_user(self, username, password):
        user_login = database.user_login(username=username, passsword=password)
        if self.username == user_login[1] and self.password == user_login[2]:
            print(f"welcome {self.username}")
            display.user_log_in_display()
            choices = inputs.choice()
            if choices == 1:
                obj_admin.vehicle_entry()
            elif choices == 2:
                obj_admin.vehicle_out()
            else:
                print("sorry invaid input exiting")
                sys.exit(-1)
        else:
            print("sorry invalid username or password")
            sys.exit(0)
        os.system("cls")

    def vehicle_entry(self):
        display.vehicle_entry_display()
        entry_inputs = inputs.vehicle_entry_inputs()
        database.vehicle_entry_details(in_date=entry_inputs[0], in_time=entry_inputs[1], name=entry_inputs[2],
                                       ph_num=entry_inputs[3], vehicle_num=entry_inputs[4], vehicle=entry_inputs[5],
                                       status=entry_inputs[6])

        display.admin_function_display()
        choice_user = inputs.choice()
        if choice_user == 1:
            obj_admin.vehicle_entry()
        elif choice_user == 2:
            obj_admin.log_in_user(username, password)
        else:
            print("invalid choice")
        os.system("cls")

    def vehicle_out(self):
        global cost_car, cost_SUV, cost_Truck, Cost_per_vehicle
        out_inputs = inputs.vehicle_out_inputs()
        database.vehicle_out_data(OUT_DATE=out_inputs[0], OUT_TIME=out_inputs[1], ph_num=out_inputs[2],
                                  vehicle_num=out_inputs[3])

        costs = database.cost()
        cost_two_wheleer = costs[0]
        cost_car = costs[1]
        cost_SUV = costs[2]
        cost_Truck = costs[3]

        vehicle = database.vehicle_type(ph_num=out_inputs[2])
        if vehicle is None:
            print("sorry no vehicle  IN \n enter vehicle before")
            obj_admin.vehicle_entry()

        elif vehicle[0] == "Two_wheeler":
            Cost_per_vehicle = cost_two_wheleer
        elif vehicle[0] == "Car":
            Cost_per_vehicle = cost_car
        elif vehicle[0] == "SUV":
            Cost_per_vehicle = cost_SUV
        elif vehicle[0] == "Truck":
            Cost_per_vehicle = cost_Truck

        day = database.days(ph_num=out_inputs[2])

        if day[0] == 0:
            Cost = Cost_per_vehicle
            print(f"Total cost of parking is {Cost}Rs for the day ")

            database.update_cost(Cost, ph_num=out_inputs[2])
            print("vehicle moved out....")
        else:

            days = day[0]
            Cost = int(days * Cost_per_vehicle)

            print(f"Total cost of parking is {Cost}Rs for {days}days ")

            database.update_cost(Cost, ph_num=out_inputs[2])
            print(f"vehicle {'vehicle num :', out_inputs[3]} moved out....")
        os.system("cls")

        display.admin_function_display()
        choice_user = inputs.choice()
        if choice_user == 1:
            obj_admin.vehicle_out()
        elif choice_user == 2:
            obj_admin.log_in_user(username, password)
        else:
            print("invalid choice")


# _______________________________________________________________________________________________________________________________________________________________________________________

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class AdminUser(User):
    def __init__(self, username, password):
        User.__init__(self, username, password)

    def login_admin(self):
        admin_login = database.admin_login()

        if self.username == admin_login[1] and self.password == admin_login[2]:
            print("")
            print("\t" * 15, f"welcome {self.username}")
            display.admin_log_in_display()
            choice_user = inputs.choice()
            if choice_user == 1:
                obj_admin.vehicle_entry()
            elif choice_user == 2:
                obj_admin.vehicle_out()
            elif choice_user == 3:
                obj_admin.search_user()
            elif choice_user == 4:
                obj_admin.details_of_parking_system()
            elif choice_user == 5:
                obj_admin.reports()
            elif choice_user == 6:
                obj_admin.collections()
            elif choice_user == 7:
                obj_admin.settings()
            elif choice_user == 8:
                sys.exit(0)

            else:
                sys.exit(0)
        else:
            print("sorry invalid username or password")
            sys.exit(0)
        os.system("cls")

    @staticmethod
    def create_admin_user():
        try:
            admin_inputs = inputs.registration_inputs()
            database.admin_details(date=admin_inputs[0], username=admin_inputs[1], password=admin_inputs[2])

            spacing = inputs.spacing_inputs()
            database.insert_vehicle_spacing(two_wheeler_spacing=spacing[0], car_spacing=spacing[1],
                                            SUV_spacing=spacing[2],
                                            Truck_spacing=spacing[3])
            cost = inputs.cost_inputs()
            database.insert_cost_allocation(cost_two_wheleer=cost[0], cost_car=cost[1], cost_SUV=cost[2],
                                            cost_Truck=cost[3])

            display.created_database_and_admin()
            raise NameError

        except NameError:
            print("pls log in before continue.\n existing system".upper())

        os.system("cls")

    def search_user(self):
        inputs.search_user_inputs()
        display.search_user_choice_display()
        choice_user = inputs.choice()
        if choice_user == 1:
            obj_admin.login_admin()
        elif choice_user == 2:
            obj_admin.search_user()
        else:
            sys.exit(0)

    def details_of_parking_system(self):
        display.parking_system_details_display()
        display.admin_function_display()
        choice_user = inputs.choice()
        if choice_user == 1:
            obj_admin.login_admin()
        elif choice_user == 2:
            obj_admin.details_of_parking_system()
        else:
            sys.exit(0)

    def reports(self):
        display.reports_display()
        choice_user = inputs.choice()
        if choice_user == 1:
            date = inputs.daily_input()
            daily_report = database.daily_reports(date=date)
            if daily_report is None:
                print("sorry no records ...")
            else:
                print(daily_report)

        elif choice_user == 2:
            month, year = inputs.monthly_input()
            monthly = database.monthly_reports(month, year)
            if monthly is None:
                print("sorry no records ...")
            else:
                print(monthly)

        elif choice_user == 3:
            year = inputs.yearly_input()
            yearly = database.yearly_reports(year)
            print(yearly)
        elif choice == 4:
            obj_admin.login_admin()
        display.admin_function_display()
        choice_user1 = inputs.choice()
        if choice_user1 == 1:
            obj_admin.login_admin()
        elif choice_user1 == 2:
            obj_admin.reports()
        else:
            sys.exit(0)

    def collections(self):
        display.collection_display()
        choice_user = inputs.choice()
        if choice_user == 1:
            date = inputs.daily_input()
            daily_report = database.daily_collections(date=date)
            if daily_report is None:
                print("sorry no records ...")
            else:
                print(f"{date} total day collectins is : {daily_report[0]}", "rs")

        elif choice_user == 2:
            month, year = inputs.monthly_input()
            monthly = database.monthly_collections(month, year)
            if monthly is None:
                print("sorry no records ...")
            else:
                print(f"{month, year} total month collections is : {monthly[0]}", "rs")

        elif choice_user == 3:
            year = inputs.yearly_input()
            yearly = database.yearly_collections(year)
            if yearly is None:
                print("sorry no records ...")
            else:
                print(f"{year} total year collectins is : {yearly[0]}", "rs")
        else:
            obj_admin.login_admin()

        display.admin_function_display()
        choice_user1 = inputs.choice()
        if choice_user1 == 1:
            obj_admin.login_admin()
        elif choice_user1 == 2:
            obj_admin.collections()
        else:
            sys.exit(0)

    def settings(self):
        display.settings_display()
        choice_user = inputs.choice()
        if choice_user == 1:
            new_password, old_password = inputs.password_change_inputs()
            database.admin_password_update(password=new_password, old_password=old_password)
            print("succefully updated")
        elif choice_user == 2:
            two_wheleer, car, SUV, Truck = inputs.space_update_inputs()
            database.parking_system_space_update(two_wheleer=two_wheleer, car=car, SUV=SUV, Truck=Truck)
            print("succefully updated")

        elif choice_user == 3:
            two_wheleer_cost, Car_cost, SUV_cost, Truck_cost = inputs.cost_update_inputs()
            database.parking_system_cost_update(two_wheleer_cost, Car_cost, SUV_cost, Truck_cost)
        else:
            sys.exit(0)

        display.admin_function_display()
        choice_user1 = inputs.choice()
        if choice_user1 == 1:
            obj_admin.login_admin()
        elif choice_user1 == 2:
            obj_admin.settings()
        else:

            sys.exit(0)


class ReportUser:
    def parking_details(self):
        display.report_user_display()


if DATABASE.exists():

    import inputs
    from database import DataBaseQueries
    import display

    database = DataBaseQueries()
    display.main_display()
    obj_admin = AdminUser

    choice = inputs.choice()

    if choice == 1:
        username, password = inputs.login_inputs()
        obj_admin = AdminUser(username, password)
        obj_admin.login_admin()

    elif choice == 2:
        username, password = inputs.login_inputs()
        user_login = database.user_login(username, password)
        print("checking for user.....")
        if user_login is None:
            print("user not available pls proceed")
            obj_admin.user_registration()
        elif user_login[1] == username:
            if user_login[2] == password:
                print("user already register .. pls log in ")
                obj_admin = User(username, password)
                obj_admin.log_in_user(username, password)

    elif choice == 3:
        obj_admin = AdminUser
        username, password = inputs.login_inputs()
        user_login = database.user_login(username, password)
        if user_login is None:
            display.user_re_log_in_diplay()
            choice = inputs.choice()
            if choice == 1:
                username, password = inputs.login_inputs()
                user_login = database.user_login(username, password)

                if user_login is None:
                    print("sorry exiting...")
                else:
                    obj_admin = User(username, password)
                    obj_admin.log_in_user(username, password)
            else:
                obj_admin.user_registration()
        else:
            obj_admin = User(username, password)
            obj_admin.log_in_user(username, password)
    elif choice == 4:
        obj_report_user = ReportUser()
        obj_report_user.parking_details()

elif not DATABASE.exists():

    from database import DataBaseInitialization

    initialization_of_database = DataBaseInitialization()
    from database import DataBaseQueries

    database = DataBaseQueries()
    import inputs
    import display

    AdminUser.create_admin_user()
