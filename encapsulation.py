
class employee: 
    def __init__(self, name, salary, bonus):
         self.name = name       # public attribute 
         self._salary = salary  # protected attribute 
         self.__bonus = bonus   # private attribute

    #Public Method
    def get_details(self):
         print(f"Name: {self.name}")
         print(f"Salary: {self._salary}")
         print(f"Bonus: {self.__bonus}")
    

    #private method
    def _calculate_total_pay(self):
         return self._salary + self.__bonus
    
    #public method accesing a private one 
    def get_total_pay(self):
         return self._calculate_total_pay
    


emp = employee('shreet', 500000, 120000)

print(emp.get_details())

print(emp.get_total_pay)

# accessing a proctected attribute
# works but not the best practice
print(emp._salary)   

''' AttributeError: 'employee' object has no attribute '__bonus' '''
# gives an error because of accessing a private attribute method

# print(emp.__bonus)

''' nothing is restricted in python (this is way to access the private attribute known as namling ) but this is a not way to use it 
 it is just to tell the developers that this is a private variable do not access it'''
print(emp._employee__bonus)