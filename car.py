class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptible_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    def read_odometer(self):
        print(f' bla bla {self.odometer_reading}')
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('don`t roll back')
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f'this car has {self.battery_size} kWh')
    def get_range(self):
        range = 0
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'this car go about {range}  miles on a full charge')

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

