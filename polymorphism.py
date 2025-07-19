''' POLYMORPHISM '''

# METHOD OVERRIDING 
class Animal:
    def speak(self):
        print('Animal makes a sound')

class dog(Animal):
    def speak(self):
        print('Dog barks') # overriding the method of the animal class 

class cat(Animal):
    def speak(self):
        super().speak() # calling the method's action from the Animal class
        print('cat meows') #overriding the method of the Animal class


a1 = Animal()
a2 = dog()
a3 = cat()

a1.speak() 
a2.speak() 
a3.speak() 

#OUTPUT 
'''
Animal makes a sound
Dog barks
Animal makes a sound
cat meows

'''

# METHOD OVERLOADING : 
# is not fully supported in python, so we take the help of *args, default parameter and Type checks


class Invoice:
    def generate_total(self, *prices, discount=0):
        total = sum(prices)
        print(f"Subtotal: Rs.{total}")
        if discount:
            discount_amount = (discount / 100) * total
            total -= discount_amount
            print(f"Discount Applied: {discount}% : Rs.{discount_amount}")
        print(f"Total Payable: Rs.{total}")
        print("-" * 30)


bill = Invoice()

bill.generate_total(200, 300, 100)                      # No discount
bill.generate_total(1000, 500, discount=10)             # With 10% discount
bill.generate_total(discount=5)  
 
#OUTPUT 

'''
Subtotal: Rs.600
Total Payable: Rs.600
------------------------------
Subtotal: Rs.1500
Discount Applied: 10%
Total Payable: Rs.1350.0
------------------------------
Subtotal: Rs.0
Discount Applied: 5%
Total Payable: Rs.0.0
------------------------------
'''