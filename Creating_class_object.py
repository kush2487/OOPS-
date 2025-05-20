class car : 
    def __init__(self, color):
        self.color = color
    def drive(self):
        print("the car is driving")

my_car = car('red')
print(my_car)
print(my_car.color)
my_car.drive()
