# A module is simply a file containing python code in it. that can include function, class and variables. Modules allow you to break down  large programs into smaller and more manageable files.

from math import pi
import sys
import random as rdm 
from rps7 import rock_paper_scissors
# print(f"The value of pi is {pi:.5f}")

# rdm.choice([1,2,3])

# print(rdm.choice([1,2,3]))

# for item in dir(rdm):

#     print(item)
# print(rdm.randint(1,50))

# print(rdm.choice(['raj','suryaraj','sury']))

# print(rdm.sample(['raj','suryaraj','sury'],k=2))

# def fib2(n):
#     """Return Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result

# print(fib2(100))

# fib2.doc

rock_paper_scissors()


