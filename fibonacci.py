"""
Fibonacci Sequence Calcualtor ("Double Method" + "Binet Formula")
Author: Parad0x
Created on: 3/24/2022
v4

------DOBULE FORMULAS------
F(2k) = F(k)[2F(k+1)-F(k)]
F(2k+1) = F(k+1)^2+F(k)^2

--------------BINET FORMULA--------------
F(k) = ((1+5^.5/2)^k - (1-5^.5/2)^k)/5^.5

We only use the binet formula when k is < 1474, due to floats being unable to hold such large numbers encountered afterwards
"""
from math import log10
from time import perf_counter

num_to_find = input("Which number are you looking for? ")
if not num_to_find.isdecimal() or 0 == int(num_to_find) :
    print("Invalid input, good bye.")
    exit(0)

num_to_find = int(num_to_find)
SQRT1,SQRT2,SQRT5 = (1+5**.5)/2,(1-5**.5)/2,(5**.5)

def get_doubled(num:int) -> tuple:
    """
    Returns a tuple of the nth fibonacci number requested and the next one in sequence
    """
    if num.__eq__(0):return (0, 1)
    c, n = get_doubled(num // 2)
    cD, nD = c * ((2*n) - c), c**2 + n**2

    if (num % 2).__eq__(0):return (cD, nD)
    return (nD, cD + nD)

def getNumber(num:int) -> int:
    """
    Returns the nth fibonacci number as an int
    """
    if num > 1474:return get_doubled(num)[0]
    return int((SQRT1**num - SQRT2**num)//SQRT5)

start = perf_counter()
answer = getNumber(num_to_find)
end = perf_counter()

print(f"Found the #{num_to_find:,d} fibonacci number in {round(end-start, 8)} seconds\n")
if (num_to_find >= 1000):
    digits = int(log10(answer))
    answer = f"{int(answer / pow(10, digits-5)):.5E}".split('E')[0]
    print (f"{str(answer)}e{digits:,d}")
else:
    print (f"{answer:,d}")