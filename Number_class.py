class Number():
    def __init__(self, number):
        self.__number = number
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, value):
        self.__number = value
    def is_even(self):
        return self.number % 2 == 0
    def is_palindrome(self):
        num_str = str(abs(self.number))
        return num_str == num_str[::-1]
    def is_prime(self):
        result = True
        for index in range(2, self.__number):
            if self.__number % 2 == 0:
                result = False
                break
        return result