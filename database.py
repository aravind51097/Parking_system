"""Creating database for paking system"""

import sqlite3
from pathlib import Path

path = Path(f"parking_system.db")


class DataBaseInitialization:

    def __init__(self):
        self.connector = sqlite3.connect(f"parking_system.db")
        self.c = self.connector.cursor()

        # create a table for customer details
        self.c.execute("""CREATE TABLE customers(
                             In_date timestamp,
                             IN_time timestamp,
                             name text,
                             ph_num text,
                             vehicle_num text,
                             vehicle_type text,
                             Cost integer,
                             status NULL,
                             Exit_date NULL,
                             Exit_time NULL
                             )
                 """)

        # create a table for end_user
        self.c.execute("""CREATE TABLE end_user(
                                                date timestamp,
                                                user_name text,
                                                password text
                                                )
                                    """)
        # create a table for admin details
        self.c.execute("""CREATE TABLE admin(
                                        date timestamp,
                                        user_name text,
                                        password text
                                        )
                            """)

        # create a table for parking_space details
        self.c.execute("""CREATE TABLE parking_space(
                                                   Two_wheeler text,
                                                   Car text,
                                                   SUV text,
                                                   Truck text
                                                   )
                                       """)

        # create a table for cost_allocation details
        self.c.execute("""CREATE TABLE cost_allocation(
                                                           Two_wheeler integer,
                                                           Car integer,
                                                           SUV integer,
                                                           Truck integer
                                                           )
                                                   """)

        print("data_base created successfully  :-) \n")
        data = "pls create admin and describe parking system terms : \nthank you..:-)\n".upper()
        print(data)


class DataBaseQueries:
    def __init__(self):
        self.connector = sqlite3.connect(f"parking_system.db")
        self.c = self.connector.cursor()

    # ______________________________________________________________________________________________________________________

    """                                             INSERT Queries                                                                        """

    # _______________________________________________________________________________________________________________________

    def end_user_details(self, date, username, password):
        self.c.execute("""INSERT INTO end_user VALUES(?,?,?)""", [date, username, password])
        print("success")
        self.connector.commit()

    def admin_details(self, date, username, password):
        self.c.execute("""INSERT INTO admin VALUES(?,?,?)""", [date, username, password])
        self.connector.commit()

    def insert_cost_allocation(self, cost_two_wheleer, cost_car, cost_SUV, cost_Truck):
        self.c.execute(""" INSERT INTO cost_allocation VALUES (?,?,?,?)""",
                       [cost_two_wheleer, cost_car, cost_SUV, cost_Truck])
        self.connector.commit()

    def insert_vehicle_spacing(self, two_wheeler_spacing, car_spacing, SUV_spacing, Truck_spacing):
        self.c.execute(""" INSERT INTO parking_space VALUES (?,?,?,?)""",
                       [two_wheeler_spacing, car_spacing, SUV_spacing, Truck_spacing])

        self.connector.commit()

    def vehicle_entry_details(self, in_date, in_time, name, ph_num, vehicle_num, vehicle, status):
        # vehicle entry details
        self.c.execute("""INSERT INTO customers VALUES(?,?,?,?,?,?,?,?,?,?)""",
                       [in_date, in_time, name, ph_num, vehicle_num, vehicle, None, status, None, None])
        self.connector.commit()

    # _________________________________________________________________________________________________________________________________________

    """                                               UPDATE Queries                                         """

    # __________________________________________________________________________________________________________________________________________

    def vehicle_out_data(self, OUT_DATE, OUT_TIME, ph_num, vehicle_num):
        self.c.execute("""UPDATE  customers 
                                              SET status="OUT",Exit_date=?,Exit_Time=? 
                                              WHERE ph_num=? AND vehicle_num=? AND
                                              Exit_Time IS NULL """, [OUT_DATE, OUT_TIME, ph_num, vehicle_num])
        self.connector.commit()

    def update_cost(self, cost, ph_num):
        self.c.execute("""UPDATE  customers SET Cost=? WHERE ph_num=? and Cost IS NULL """, [cost, ph_num])
        self.connector.commit()

    def admin_password_update(self, password, old_password):
        self.c.execute(""" UPDATE admin SET password=? WHERE password=? """, [password, old_password])
        self.connector.commit()

    def parking_system_space_update(self, two_wheleer, car, SUV, Truck):
        self.c.execute(""" UPDATE parking_space SET Two_wheeler=?, Car=?,SUV=?,Truck=? """,
                       [two_wheleer, car, SUV, Truck])
        self.connector.commit()

    def parking_system_cost_update(self, two_wheleer_cost, Car_cost, SUV_cost, Truck_cost):
        self.c.execute(""" UPDATE cost_allocation SET Two_wheeler=?, Car=?,SUV=?,Truck=? """,
                       [two_wheleer_cost, Car_cost, SUV_cost, Truck_cost])
        self.connector.commit()

    # ______________________________________________________________________________________________________________________

    """                        ***** SELECT Queries *****                                                                        """

    # _______________________________________________________________________________________________________________________

    def user_login(self, username, passsword):
        self.c.execute(""" SELECT * FROM end_user WHERE  user_name=? AND password=? """, [username, passsword])

        datas = self.c.fetchall()

        for data in datas:
            return data

    def admin_login(self):
        self.c.execute(""" SELECT * FROM admin""")

        datas = self.c.fetchall()

        for data in datas:
            return data

    def parking_space(self):
        # fetching the spacing details from parking_space table
        self.c.execute(""" SELECT * FROM parking_space  """)
        spaces = self.c.fetchall()

        for space in spaces:
            return space

    def space_availabe(self, vehicle_type):
        # fetching the available space details from customers table based on vehicle IN
        self.c.execute(""" SELECT COUNT(name) FROM customers WHERE vehicle_type=? and status="IN" """,
                       [vehicle_type])
        counts = self.c.fetchall()
        for count in counts:
            return count

    def vehicle_status(self, vehicle_num):
        self.c.execute(""" SELECT vehicle_num FROM customers WHERE vehicle_num=? and status="IN" """, [vehicle_num])
        status = self.c.fetchall()
        return status

    def cost(self):
        self.c.execute("""SELECT * FROM cost_allocation""")

        cost_per_vehicles = self.c.fetchall()

        for cost_per_vehicle in cost_per_vehicles:
            return cost_per_vehicle

    def vehicle_type(self, ph_num):
        self.c.execute("""select  vehicle_type from customers WHERE ph_num=? and Cost IS NULL """, [ph_num])

        vehicle_types = self.c.fetchall()

        for vehicle_type in vehicle_types:
            return vehicle_type

    def days(self, ph_num):
        self.c.execute(
            'select JULIANDAY(Exit_date) - JULIANDAY(IN_date) AS date_difference from customers where ph_num=?',
            [ph_num])

        parking_days = self.c.fetchall()

        for day in parking_days:
            return day

    def user_details(self, ph_num, vehicle_num):
        self.c.execute(""" SELECT * FROM customers WHERE ph_num=? AND vehicle_num=? """, [ph_num, vehicle_num])

        user_detail = self.c.fetchall()
        for i in user_detail:
            lst = []
            for j in i:
                lst.append(j)
            return lst

    def daily_reports(self, date):
        self.c.execute(""" SELECT rowid,* FROM customers WHERE In_date=? """, [date])

        daily_report = self.c.fetchall()

        for i in daily_report:
            return i

    def monthly_reports(self, month, year):
        self.c.execute(
            """ SELECT rowid, * FROM customers WHERE  strftime('%m',IN_date)= ? AND strftime('%Y',IN_date)= ?""",
            [month, year])

        monthly_report = self.c.fetchall()

        for i in monthly_report:
            return i

    def yearly_reports(self, year):
        self.c.execute(""" SELECT rowid, * FROM customers WHERE  strftime('%Y',IN_date)= ?""", [year])

        yearly_report = self.c.fetchall()
        for i in yearly_report:
            return i

    def daily_collections(self, date):
        self.c.execute(""" SELECT SUM(cost) FROM customers WHERE In_date=? """, [date])

        daily_collection = self.c.fetchall()
        for i in daily_collection:
            return i

    def monthly_collections(self, month, year):
        self.c.execute(
            """ SELECT SUM(cost) FROM customers WHERE strftime('%m',IN_date)= ? AND strftime('%Y',IN_date)= ? """,
            [month, year])

        monthly_colection = self.c.fetchall()
        for i in monthly_colection:
            return i

    def yearly_collections(self, year):
        self.c.execute(""" SELECT SUM(cost) FROM customers WHERE strftime('%Y',IN_date)= ? """, [year])

        year_collection = self.c.fetchall()
        for i in year_collection:
            return i


if __name__ == "__main__":
    pass
