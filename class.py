# user_peter = {
#     "name": "Peter",
#     "email": "peterrobertson@mail.com",
#     "created_at": "2019-05-05",
#     "is_email_verified": True,
#     "purchases": ["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"],
# }
#
# user_julia = {
#     "name": "Julia Donaldson",
#     "email": "juliadonaldson@mail.com",
#     "created_at": "2019-06-13",
#     "is_email_verified": True,
#     "purchases": ["Egg", "Spam", "Magic Brush"],
# }
#
# product_eggs = {
#     "name": "Egg",
#     "category": "food",
#     "is_available": False,
#     "quantity_in_stock": 0,
#     "vendor": "Dark Knight LTD",
#     "manager": "William The Conqueror",
# }
#
#
# class User:
#     pass
#
#
# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#
# events = [
#     {
#         "timestamp": 1554583508000,
#         "type": "itemViewEvent",
#         "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#         "timestamp": 1555296337000,
#         "type": "itemViewEvent",
#         "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#         "timestamp": 1549461608000,
#         "type": "itemBuyEvent",
#         "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
#
# for event in events:
#     event_obj = Event(timestamp=event.get("timestamp"),
#                       event_type=event.get("type"),
#                       session_id=event.get("session_id"))
#     print(event_obj.timestamp)
#
# print(user_julia['name'])

# class Human():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# my_human = Human('jullie', 33)
#
# print(f'{my_human.name} {my_human.age}')
#

# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type
#     def describe_restaurant(self):
#         print(f'ресторан "{self.name}" открыт') if self.type == 'open' else print(f'ресторан "{self.name}" закрыт')
#
#
#
# my_restoraunt = Restaurant('bar', 'open')
# # print(f'{my_restoraunt.name}')
# my_restoraunt.describe_restaurant()
#
# my_cafe = Restaurant('cafe', 'close')
# my_cafe.describe_restaurant()
# my_burger = Restaurant('burger', 'open')
# my_burger.describe_restaurant()

# class User():
#     def __init__(self, first_name, last_name):
#         self.name = first_name
#         self.surname = last_name
#
#     def greet_user(self):
#         print(f'Good day, {self.name}')
#
#     def describe_user(self):
#         print(f'Пользователь: {self.name} {self.surname}')
#
# first_user = User('glad','kalitka')
# sec_user = User('Vlad','kalitka')
# thrd_user = User('Timle','Blad')
#
# first_user.greet_user()
# first_user.describe_user()
# sec_user.greet_user()
# sec_user.describe_user()
# thrd_user.greet_user()
# thrd_user.describe_user()


# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptible(self):
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name.title()
#
# my_new_car = Car('kia', 'soul', 2019)
# print(my_new_car.get_descriptible())



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

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model X', 2020)
print(my_tesla.get_descriptible_name())

