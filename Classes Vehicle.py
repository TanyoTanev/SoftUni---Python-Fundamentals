'''* Vehicle

Create a class Vehicle. The __init__ method should receive: type, model, price. You should also set the owner to None.
The class should have the following methods:
buy(money, owner) - if the person has enough money and the vehicle has no owner, returns:
"Successfully bought a {type}. Change: {change}" and sets the owner to the given one.
If the money is not enough, return: "Sorry, not enough money". If the car already has an owner, return: "Car already sold"
sell() - if the car has an owner, set it to None again. Otherwise, return: "Vehicle has no owner"
__repr__() - returns "{model} {type} is owned by: {owner}" if the vehicle has an owner. Otherwise, return: "{model} {type} is on sale: {price}"

Example
Test Code
Output

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)
Sorry, not enough money
Successfully bought a car. Change: 5000.00
BMW car is owned by: George
BMW car is on sale: 30000'''

class Vehicle:

    def __init__(self,type, model, price, owner = None):
        self.type = type
        self.model = model
        self. price = price
        self. owner = owner

    def buy(self, money, owner):
        result = ""
        if self.owner != None:
            result = "Car already sold"
            return result

        elif money >= self.price:

            self.owner = owner
            result = f'Successfully bought a {self.type}. Change: {(-self.price + money):.2f}'
            return result
        #result =
        return "Sorry, not enough money"

    def sell(self):
        result = ""
        if self.owner !=None:
            self.owner = None
            return
        result = "Vehicle has no owner"
        return result
    def __repr__(self):
        result = ""
        if self.owner != None:
            result = f"{self.model} {self.type} is owned by: {self.owner}"
            return result
        result = f"{self.model} {self.type} is on sale: {self.price}"
        return result


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)