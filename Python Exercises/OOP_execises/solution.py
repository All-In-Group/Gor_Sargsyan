#Question 1
'''
Exercise Question 1: Create a Vehicle class with max_speed and mileage instance attributes
'''
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def __str__(self):
        return f"Max speed is {self.max_speed}\nMileage is {self.mileage}\n"

My_vehicle = Vehicle(max_speed=230,mileage=40)
print(My_vehicle)

#Question 2
'''
Exercise Question 2: Create a Vehicle class without any variables and methods
'''
class Vehicle:
    pass

Vehicle_2 = Vehicle
print(f"{Vehicle_2} is without any variables and methods\n")


#Question 3
'''
Exercise Question 3: Create child class Bus that will inherit all of the variables and methods of the Vehicle class
'''
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def Method(self):
        print(f"this Method is called from super class {Vehicle.__name__} by class {self.__class__.__name__}\n")

class Bus(Vehicle):
    pass

My_Buss = Bus(200,10)
My_Buss.Method()

#Question 4
'''
Exercise Question 4: Class Inheritance
Given:

Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class. You need to use method overriding.
'''

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def __init__(self,name,max_speed,mileage,capacity = 50):
        super().__init__(name,max_speed,mileage)
        self.capacity = capacity
    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers\n"

My_Buss = Bus("Mercedes Bus",200,30)
print(My_Buss.seating_capacity())

#Question 5
'''
exercise Question 5: Define property that should have the same value for every class instance
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

Use the following code for this exercise.
'''
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self,name,max_speed,mileage,colour = "white"):
        super().__init__(name,max_speed,mileage)
        self.colour = colour
    def __str__(self):
        return f"{self.name} colour is  {self.colour}"


class Car(Vehicle):
    def __init__(self,name,max_speed,mileage,colour = "white"):
        super().__init__(name,max_speed,mileage)
        self.colour = colour

    def __str__(self):
        return f"{self.name} colour is  {self.colour}"

my_bus = Bus("Mercedes Bus",200,20)

my_car = Car("Mercedes Car",200,20)

print(my_bus,"\n",my_car,"\n")

#Question 6
'''
Exercise Question 7: Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is 

seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 

So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5550. You need to override the fare() method of a Vehicle class in Bus class.

Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.


'''
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        total = super().fare()
        return total + total * 10/100

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

#Question 7

'''
Exercise Question 7: Determine which class a given Bus object belongs to (Check type of a object)
'''
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    def __type__(self):
        return "hugachaga"

School_bus = Bus("School Volvo", 12, 50)

print(School_bus.__class__)

#Question 8
'''

'''
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(issubclass(Bus,Vehicle))
