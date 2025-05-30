
#simple inheritance example
class Vehicle():    #parent class
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        print(f"{self.brand} is moving ")

class car(Vehicle): #child  1 class inheriting the behaviour of the parent class vehicle 
    def play_music(self):
        print(f'{self.brand} is playing music')

class bike(Vehicle):    #child 2 class inheriting the behaviour of the parent class vehicle 
    def do_wheelie(self):
        print(f"{self.brand} can do wheelie")

my_car = car('kia')
print(my_car.brand)
my_car.move() # its own feature
''' 
output : 
kia
kia is moving '''

my_bike = bike('yamaha')
print(my_bike.brand)
my_bike.do_wheelie() # its own feature'
'''
output:
yamaha
yamaha can do wheelie'''




''' Single Inheritance '''
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):  # Inherits from Vehicle
    def drive(self):
        print("Car is driving")


''' Multiple Inheritance '''
class MusicSystem:
    def play_music(self):
        print("Playing music")

class SmartCar(Vehicle, MusicSystem):  # Inherits from 2 parents
    def gps(self):
        print("GPS is on")


''' Multilevel Inheritance '''
class Engine:
    def engine_info(self):
        print("Engine is powerful")

class SportsCar(Engine):  # Parent
    def top_speed(self):
        print("Top speed: 300km/h")

class SuperSportsCar(SportsCar):  # Child of child
    def nitro(self):
        print("Nitro Boost Activated!")


''' Hierarchical Inheritance'''
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):  # Different child
    def bark(self):
        print("Bark!")

class Cat(Animal):
    def meow(self):
        print("Meow!")


''' Hybrid Inheritance = Mix (handled using MRO) '''
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  # Hybrid – inherits from B and C
    pass


# ----- TESTING ALL TOGETHER -----
print("\nSINGLE:")
car = Car()
car.start()
car.drive()

print("\nMULTIPLE:")
sc = SmartCar()
sc.start()
sc.play_music()
sc.gps()

print("\nMULTILEVEL:")
ssc = SuperSportsCar()
ssc.engine_info()
ssc.top_speed()
ssc.nitro()

print("\nHIERARCHICAL:")
dog = Dog()
cat = Cat()
dog.sound()
dog.bark()
cat.sound()
cat.meow()

print("\nHYBRID:")
d = D()
print(d.mro())
d.show()  # Will follow MRO → B before C
