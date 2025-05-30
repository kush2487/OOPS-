class BankUtils:

    @staticmethod # decorator
    def calculate_interest(principal, rate, time):
        """
        Simple Interest = (P * R * T) / 100
        """
        interest = (principal * rate * time) / 100
        return interest

# Test Cases
print("Interest:", BankUtils.calculate_interest(10000, 5, 2))   # Rs.1000
print("Interest:", BankUtils.calculate_interest(5000, 7, 1))    # Rs.350


class math:
    @staticmethod #decorator
    def add(a,b):
        return a+b 

p = math.add(2,3)
print("the sum is : ", p)

