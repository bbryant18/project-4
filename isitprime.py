#!/usr/bin/env python

# Fixed issues

a = input("Pick a number: ")
# make sure n is a positive integer
n = abs(int(a))
# Counter used to help determine if number is prime or not
y = 0

# 0 and 1 are not primes
if n < 2:
    y += 1

  # 2 is the only even prime number
elif n == 2:
    y = 0

    # all other even numbers are not primes
elif not n & 1:
    y += 1

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers

for x in range(3, int(n**0.5) + 1, 2):
    if n % x == 0:
      y = y + 1
      break

if y >= 1:
        print("Not Prime")
else:
        print("Prime")
