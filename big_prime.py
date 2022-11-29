"""
    This program finds the x_th prime number really fast
    Author: Parad0x
    v2.4
    E.g:
    Which prime number are you looking for? 100000
    The 100000-th prime number is 1299709
    This took 12.828526597004384 seconds
"""

from time import perf_counter

x = input("Which prime number are you looking for? ")
if not x.isdecimal() or 0 == int(x) :
    print("Invalid input, good bye.")
    exit(0)
number_of_primes = int(x)

num_to_check = 1
prime_counter = 1
prime_numbers = [2]

start = perf_counter()
while prime_counter < number_of_primes:
    num_to_check += 2
    g = int(num_to_check**.5)
    for i in prime_numbers:
        if not num_to_check % i:
            break
        if (i >= g):
            prime_numbers += [num_to_check]
            prime_counter += 1
            break        
end = perf_counter()

print(f"""The {number_of_primes}th prime number is {prime_numbers[-1]}
This took {end-start} seconds\n""")