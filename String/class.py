class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def display(self):
        return 'Name: ' + self.__name



'''
Якщо необхідно отримати доступ до атрибуту, використовується метод, над назвою якого ставиться анотація @property:

@property
def name(self):
    return self.__name
Відповідно, для зміни значення атрибута використовується інший метод з таким же ім’ям, але над назвою якого записується 
анотація назва_методу_для_отримання_значення_атрибута.setter:

@name.setter
def name(self, name):
    self.__name = name
'''




class Car():
    """Проста модель автомобіля."""
    def __init__(self, make, model, year):
        """Ініціалізація атрибутів опису автомобіля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Повертає опис у відформатованому вигляді."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Виводить пробіг автомобіля у км."""
        print("This car has " + str(self.odometer_reading) + " kilometers on it.")

    def update_odometer(self, km):
        """Встановлення заданого значення на одометрі.
        При спробі зворотного прокручування зміна відхиляється."""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, kkm):
        """Збільшує показники одометра із заданим збільшенням."""
        self.odometer_reading += kkm

def fill_petrol_tank(self):
        """Виводить інформацію про наяність бака для бензину."""
        print("This car is equipped with a petrol tank.")


class ElectricCar(Car):
    """Представляє аспекти автомобіля, специфічні для електромобілів."""
    def __init__(self, make, model, year):
        """Ініціалізує атрибути класу-батька.
        Потім ініціалізує атрибути, специфічні для електромобіля."""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Виводить інформацію про потужність акумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

def fill_petrol_tank(self):
        """У електромобілів немає бензобаку."""
        print("This car doesn't need a petrol tank!")


my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()