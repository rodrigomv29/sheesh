import math
def isPrime(num):
    sqrt_num = math.sqrt(num)
    for i in range(2, sqrt_num):
        if num % 2 == 0:
            return False
        continue

