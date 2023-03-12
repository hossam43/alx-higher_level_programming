#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print("{} is zero".format(number))
elif number < 0:
    print("{} is negtive".format(number))
elif number > 0:
    print("{} is postive".format(number))
