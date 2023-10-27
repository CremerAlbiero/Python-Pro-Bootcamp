#python modules
import random

random_int = random.randint(1, 20)
print(random_int)

#random floating numbers (just generate between 0.0 0.9)
random_float = random.random()
print(random_float)

#combining example:
random_float = random_float + random.randint(1, 5)
print(random_float)