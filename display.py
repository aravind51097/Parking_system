from database import DataBaseQueries

database = DataBaseQueries()

sparator = ("*" * 150)


def main_display():
    print("")
    sparators = ("*" * 150)
    print(sparators)
    print("\t" * 14, "welcome to the parking system ")
    print(sparators)
    print("""
            1.Admin log IN
            2.New User registration 
            3.User Log IN
            4.parking details
               
            """)
    print(sparators)
    print(sparators)


def user_re_log_in_diplay():
    print("sorry no user available")
    print("""
                1.re_logIn
                2.create user

        """)


def created_database_and_admin():
    print("database created")
    print("admin user successfully created ")


def user_log_in_display():
    print(sparator)
    print(sparator)
    print("""             
               1.vehicle entry    
               2.vehicle OUT      
                  
                """)
    print(sparator)
    print(sparator)


def admin_log_in_display():
    print(sparator)
    print(sparator)
    print("""                   
            1.vehicle entry                
            2.vehicle OUT                  
            3.search for user              
            4.parking system details       
            5.Reports                      
            6.Collections                  
            7.Settings                     
            8.log out                      
                  
                           """)
    print(sparator)
    print(sparator)


def vehicle_entry_display():
    print(sparator)
    print(sparator)
    print("""
               --------------------------
               --------------------------
               1.two wheeler :- 20rs/day
               2.car         :- 50rs/day
               3.SUV         :- 100rs/day
               4.truck       :- 200rs/day 
               -------------------------- 
               --------------------------      
                    """)


def reports_display():
    print(""" 
                  **********************************
                  1.Daily reports                  :
                  2.monthly reports                :
                  3.yearly reports                 :
                  4.exit current menu              :
                  **********************************

              """)


def collection_display():
    print(""" 
               **************************************
               1.Daily collections                  :
               2.monthly collections                :
               3.yearly collections                 :
               4.exit current menu                          :
               **************************************
                """)


def user_details_display():
    print(sparator)
    print(sparator)
    print("| {:10s} | {:10s} | {:15s} | {:10s} | {:11s} | {:11s} | {:11s} | {:11s} | {:15s} | {:15}|".format(
        "In_date", "IN_time", "name", "ph_num", "vehicle_num", "vehicle_type", "Cost Price", "status", "Exit_date",
        "Exit_time"))


def search_user_choice_display():
    print("""\n choose the choice
                        *************************
                        -------------------------
                        1.main_menu
                        2.search for another user 
                        3.log_out   
                        -------------------------
                        *************************

        """)


def admin_function_display():
    print(sparator)
    print(sparator)
    print("""
            1.main menu
            2.continue here
            3.log Out
    
    """)
    print(sparator)
    print(sparator)


def settings_display():
    print(sparator)
    print(sparator)
    print("""
            1.change password
            2.change space details
            3.change Cost details
    
    
    """)
    print(sparator)
    print(sparator)


def parking_system_details_display():
    cost = database.cost()
    print("-" * 40)
    print("\t\t Cost details.")
    print("-" * 40)
    print("Two wheeler parking cost/day  : ", cost[0], "rs")
    print("car parking  cost/day         : ", cost[1], "rs")
    print("SUV parking  cost/day         : ", cost[2], "rs")
    print("Truck parking cost/day        : ", cost[3], "rs")

    two_wheeler_space = database.space_availabe("Two_wheeler")
    car_space = database.space_availabe("Car")
    SUV_space = database.space_availabe("SUV")
    Truck_space = database.space_availabe("Truck")
    print("-" * 40)
    print("\t\t vehicles parked ")
    print("-" * 40)

    print("total Two_wheeler parked    :", two_wheeler_space[0])
    print("total Car parked            :", car_space[0])
    print("total SUV parked            :", SUV_space[0])
    print("total Truck parked          :", Truck_space[0])

    total = database.parking_space()
    print("-" * 40)
    print("\t\tslots available")
    print("-" * 40)
    print("available two wheeler space   : ", int(total[0]) - int(two_wheeler_space[0]))
    print("available car space           : ", int(total[1]) - int(car_space[0]))
    print("available SUV space           : ", int(total[2]) - int(SUV_space[0]))
    print("available truck space         : ", int(total[3]) - int(Truck_space[0]))
    print("-" * 40)
    print("-" * 40)


def report_user_display():
    cost = database.cost()
    print("-" * 40)
    print("\t\t Cost details.")
    print("-" * 40)
    print("Two wheeler parking cost/day  : ", cost[0], "rs")
    print("car parking  cost/day         : ", cost[1], "rs")
    print("SUV parking  cost/day         : ", cost[2], "rs")
    print("Truck parking cost/day        : ", cost[3], "rs")
    total = database.parking_space()
    print("-" * 40)
    print("\t\tslots available")
    print("-" * 40)
    two_wheeler_space = database.space_availabe("Two_wheeler")
    car_space = database.space_availabe("Car")
    SUV_space = database.space_availabe("SUV")
    Truck_space = database.space_availabe("Truck")
    print("available two wheeler space   : ", int(total[0]) - int(two_wheeler_space[0], ), 'of', total[0])
    print("available car space           : ", int(total[1]) - int(car_space[0]), 'of', total[1])
    print("available SUV space           : ", int(total[2]) - int(SUV_space[0]), 'of', total[2])
    print("available truck space         : ", int(total[3]) - int(Truck_space[0]), 'of', total[3])
    print("-" * 40)
    print("-" * 40)
