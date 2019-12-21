# https://www.flyuia.com/ua/ua/information/flights-schedule#regular-timetable
# qty of plains [3, 4, 24, 4, 5, 2]

import datetime


class ModelPlane:
    """ Характеристики певної моделі літака"""

    def __init__(self, model, seats, carrying_capacity):
        """Опис характеристик даної моделі"""
        self.__model = model
        self.__seats = seats
        self.__carrying_capacity = carrying_capacity

    @property
    def model(self):
        return self.__model

    @property
    def seats(self):
        return self.__seats

    @property
    def carrying_capacity(self):
        return self.__carrying_capacity


class Plane:
    """Plane characteristic / Інформація про літак"""

    def __init__(self, board_number, model, working_hours=0):
        self.__board_number = board_number
        self.__model = model
        self.__working_hours = working_hours

    @property
    def board_number(self):
        return self.__board_number

    @property
    def working_hours(self):
        return self.__working_hours

    @working_hours.setter
    def working_hours(self, working_hours):
        try:
            if working_hours >= 0:
                self.__working_hours += working_hours
        except ValueError:
            print('Wrong value. It can\'t be less than 0')

    @property
    def model(self):
        return self.__model
    # @property
    # def board_number(self):
    #     return self.__board_number


class Flight:
    """Польоти"""
    ALLOWED = {
        'A1': [{'departure_airport': 'Lviv', 'destination_airport': 'Kyiv'},
               {'departure_airport': 'Kyiv', 'destination_airport': 'Lviv'},
               {'departure_airport': 'Lviv', 'destination_airport': 'Odesa'},
               {'departure_airport': 'Odesa', 'destination_airport': 'Lviv'}],
        'A2': [{'departure_airport': 'Lviv', 'destination_airport': 'Warsaw'},
               {'departure_airport': 'Warsaw', 'destination_airport': 'Lviv'},
               {'departure_airport': 'Lviv', 'destination_airport': 'Budapest'},
               {'departure_airport': 'Budapest', 'destination_airport': 'Lviv'}],
        'A3': [{'departure_airport': 'Lviv', 'destination_airport': 'Dubai'},
               {'departure_airport': 'Dubai', 'destination_airport': 'Lviv'},
               {'departure_airport': 'Lviv', 'destination_airport': 'Tel Aviv'},
               {'departure_airport': 'Tel Aviv', 'destination_airport': 'Lviv'}]
    }

    def __init__(self, departure_airport: str, destination_airport: str, departure_time, landing_time):
        """Характеристики кожного польоту"""
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.departure_time = departure_time
        self.landing_time = landing_time
        #self.flight_number = flight_number


class Employee:
    """працівники: profession: pilot_in_command, pilot, FlightAttendant"""

    def __init__(self, number, first_name, last_name, birth_date, address, profession):
        self.__number = number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__address = address
        self.__profession = profession
       # self.__authorized_plane_models = authorized_plane_models

    @property
    def number(self):
        return self.__number

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, profession):
        self.__profession = profession

    @property
    def authorized_plane_models(self):
        return self.__authorized_plane_models

    @authorized_plane_models.setter
    def authorized_plane_models(self, authorized_plane_models):
        self.__authorized_plane_models = authorized_plane_models


class Airport:
    pass


m1 = ModelPlane('Boeing 777-200ER', 361, 3)
m2 = ModelPlane('Boeing 767-300ER', 261, 4)
m3 = ModelPlane('Boeing  737-800', 186, 24)
m4 = ModelPlane('Boeing 737-900', 215, 4)
m5 = ModelPlane('EMBRAER-190', 104, 5)
m6 = ModelPlane('EMBRAER-195', 116, 2)
p1 = Plane('10d2', m1)
p2 = Plane('10f5', m2)
p3 = Plane('10d6', m3)
p4 = Plane('10f8', m5)
p5 = Plane('10d5', m3)
p6 = Plane('11d2', m4)
p7 = Plane('11f3', m6)
p8 = Plane('10e5', m4)
print(p1.model.model)  # має вивести M1

e1 = Employee(101, 'Vasyl', 'Ladanytsky', '12.04.1989', 'Kyiv', 'AirplaneCommander')
e2 = Employee(102, 'Andriy', 'Banas', '17.09.1982', 'Kyiv', 'Pilots')
e3 = Employee(103, 'Myron', 'Kosyk', '29.10.1985', 'Kyiv', 'Pilots')
e4 = Employee(104, 'Igor', 'Petryk', '31.07.1988', 'Kyiv', 'AirplaneCommander')
e5 = Employee(101, 'Maryna', 'Gapko', '12.04.1989', 'Kyiv', 'Stewardess')
e6 = Employee(101, 'Iryna', 'Drab', '12.04.1989', 'Kyiv', 'Stewardess')
e7 = Employee(101, 'Oksana', 'Vykrykush', '12.04.1989', 'Kyiv', 'Stewardess')
e8 = Employee(101, 'Tetiana', 'Ladanytsky', '12.04.1989', 'Kyiv', 'Stewardess')
