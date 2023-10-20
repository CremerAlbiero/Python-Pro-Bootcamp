# There are two variables, a and b from input. Make them switch values.
a = input()
b = input()

# Write your code below this line.
a, b = b, a
 
print("a: " + a)
print("b: " + b)

'''
another solution:
c = a 
a = b
b = c
'''