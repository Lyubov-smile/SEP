import random


class Train:

    def __init__(self, number, name, qty_of_wagons):
        self.__number = number
        self.__name = name
        self.__wagon = [None] * qty_of_wagons

    def random_wagon(self):
        for i in range(0, len(self.wagon)):
            self.wagon[i] = random.randrange(36)

    def __str__(self):
        return f'Train number {self.number}, destination {self.name} , Wagons {", ".join(str(x) for x in self.wagon)}'

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number

    @property
    def wagon(self):
        return self.__wagon

    def max_wagon(self):
        max_el = self.wagon[0]
        number_wagon = 0
        for i in range(1, len(self.wagon)):
            if self.wagon[i] > max_el:
                max_el = self.wagon[i]
                number_wagon = i
        return number_wagon + 1

    def min_wagon(self):
        min_el = self.wagon[0]
        number_wagon = 0
        for i in range(1, len(self.wagon)):
            if self.wagon[i] < min_el:
                min_el = self.wagon[i]
                number_wagon = i
        return number_wagon + 1

    def qty_of_passenger(self):
        s = 0
        for i in range(len(self.wagon)):
            s += self.wagon[i]
        return s

#    def qty_of_passenger(self):
#                return sum(self.wagon)


qty_train = int(input('Input the quantity of trains in your RailWay Station '))
trains = []
for i in range(qty_train):
    number = int(input('Input the number of train '))
    name = input('Input the direction of train ')
    qty_of_wagons = int(input('Input the quantity of wagons in train '))
    t = Train(number, name, qty_of_wagons)
    t.random_wagon()
    trains.append(t)

#    trains.append(Train(number, name, qty_of_wagons))

for i in range(qty_train):
    print(trains[i])

# train1 = Train(1, 'Kyiv-Lviv', 6)
# train1.random_wagon()
# print(train1)
# print(train1.max_wagon())
# print(train1.min_wagon())
# print(train1.qty_of_passenger())



