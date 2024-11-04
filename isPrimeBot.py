import math
class PrimeBot:
    def __init__(self, name):
        self.name = name
    def isPrime(self, num):
        sqrt_num = math.sqrt(num)
        for i in range(2, sqrt_num):
            if num % i == 0:
                return False
            continue

