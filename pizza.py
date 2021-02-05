# The Pizza Calculator
# Connor Williams 2021

# imported all functions from math module so I can use a more accurate pi
# decided on this vs import math for simplicity
# https://discuss.codecademy.com/t/import-math-vs-from-math-import-is-there-a-difference/43314
from math import *

# integer value of user input assigned to diameter of pizza
diameter_p = int(input("What is the diameter of your pizza in inches? "))

# float value of user input assigned to price of pizza
price_p = float(input("What is the total price of your pizza? "))

# area of the pizza using the math modules pi and area of a circle formula
# area of a circle formula given in homework 2 assignment guidelines
area_p = pi * (diameter_p / 2)**2

# cost of the pizza per square inch
cost_p = price_p / area_p

# output the cost of the pizza per square inch for the user to see
print("You entered that it costs $" + str(price_p) + " for your " + str(diameter_p) + " inch pizza.")
print("If this is true, then your pizza costs $" + str(round(cost_p, 2)) + " per square inch!")
