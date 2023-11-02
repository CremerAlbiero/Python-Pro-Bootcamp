# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hello")
    print("How are you?")
    print("Isn't the weather nice?")


#Function that allows for input

# the variable inside the parentheses, describes the data it'll receive.
def greet_with_name(name):
    print(f"Hello {name}")
    print("How are you?")
    print("Isn't the weather nice?")

greet_with_name(input("What's you name?\n"))

# Parameter x Argument
# The parameter is the name of the data that's being passed in, while the argument is the actual value of the data.