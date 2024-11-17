# it's changing the behavior depending on the context 


######### polymorphism in built-in function like len()  reversed()
###   students = ['Emma', 'Jessa', 'Kelly']
# school = 'ABC School'

# # calculate count
# print(len(students))
# print(len(school))

'''
# students = ['Emma', 'Jessa', 'Kelly']
# school = 'ABC School'

# print('Reverse string')
# for i in reversed('PYnative'):
#     print(i, end=' ')

# print('\nReverse list')
# for i in reversed(['Emma', 'Jessa', 'Kelly']):
#     print(i, end=' ')

'''

######## method overloading in built in function 

for i in range(5): print(i, end=', ')
print()
for i in range(5, 10): print(i, end=', ')
print()
for i in range(2, 12, 2): print(i, end=', ')

#########  operator overloading in built in functions
# add 2 numbers
print(100 + 200)

# concatenate two strings
print('Jess' + 'Roy')

# merger two list
print([10, 20, 30] + ['jessa', 'emma', 'kelly'])

########## method overriding ##############
class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()



####### overrriding built_in functions (magic functions ) #########

class Shopping:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        print('Redefine length')
        count = len(self.basket)
        # count total items in a different way
        # pair of shoes and shir+pant
        return count * 2

shopping = Shopping(['Shoes', 'dress'], 'Jessa')
print(len(shopping))


######### method over loading #####
   # here the method has multiple definitions with multiple different parameters through the function logic 

class Shape:
    # function with two default parameters
    def area(self, a, b=0):
        if b > 0:
            print('Area of Rectangle is:', a * b)
        else:
            print('Area of Square is:', a ** 2)

square = Shape()
square.area(5)

rectangle = Shape()
rectangle.area(5, 3)


########## + operator overloading ########
   #### change behavior of the python operator by using the underlying maic functions of the operator 

class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading + operator with magic method
    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(400)
b2 = Book(300)
print("Total number of pages: ", b1 + b2)

################### overloading the * operator

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, timesheet):
        print('Worked for', timesheet.days, 'days')
        # calculate salary
        return self.salary * timesheet.days


class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days


emp = Employee("Jessa", 800)
timesheet = TimeSheet("Jessa", 50)
print("salary is: ", emp * timesheet)

############ operator magic function 
'''
Addition	+	__add__(self, other)
Subtraction	-	__sub__(self, other)
Multiplication	*	__mul__(self, other)
Division	/	__div__(self, other)
Floor Division	//	__floordiv__(self,other)
Modulus	%	__mod__(self, other)
Power	**	__pow__(self, other)
Increment	+=	__iadd__(self, other)
Decrement	-=	__isub__(self, other)
Product	*=	__imul__(self, other)
Division	/+	__idiv__(self, other)
Modulus	%=	__imod__(self, other)
Power	**=	__ipow__(self, other)
Less than	<	__lt__(self, other)
Greater than	>	__gt__(self, other)
Less than or equal to	<=	__le__(self, other)
Greater than or equal to	>=	__ge__(self, other)
Equal to	==	__eq__(self, other)
Not equal	!=	__ne__(self, other)

'''

############
'''
Polymorphism In Class methods
Polymorphism with class methods is useful when we group different objects having the same method. we can add them to a list or a tuple, and we don’t 
need to check the object type before calling their methods. Instead, Python will check object type at runtime and call the correct method. Thus, we can call the methods
 without being concerned about which class type each object is. We assume that these methods exist in each class.

Python allows different classes to have methods with the same name.

Let’s design a different class in the same way by adding the same methods in two or more classes.
Next, create an object of each class
Next, add all objects in a tuple.
In the end, iterate the tuple using a for loop and call methods of a object without checking its class.

'''
class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

ferrari = Ferrari()
bmw = BMW()

# iterate objects of same type
for car in (ferrari, bmw):
    # call methods without checking class of object
    car.fuel_type()
    car.max_speed()



############
'''
Polymorphism with Function and Objects
We can create polymorphism with a function that can take any object as a parameter and execute its method without checking its class type.
 Using this, we can call object actions using the same function instead of repeating method calls.
'''
class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

# normal function
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()

ferrari = Ferrari()
bmw = BMW()

car_details(ferrari)
car_details(bmw)    