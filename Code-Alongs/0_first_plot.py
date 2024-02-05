from math import *
import matplotlib.pyplot as plt
numbers = list(range(10))
#list comprehension

squares = [number**2 for number in numbers]
print(numbers)
print(squares)
plt.plot(numbers , squares)
plt.title("x^2 for for positive integers 8-9")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

