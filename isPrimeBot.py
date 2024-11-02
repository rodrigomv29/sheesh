import math
def isPrime(num):
    sqrt_num = math.sqrt(num)
    for i in range(2, sqrt_num):
        if num % i == 0:
            return False
        continue

