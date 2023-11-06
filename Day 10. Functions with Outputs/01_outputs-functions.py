# Functions with Outputs

def my_function():
    result = 3 * 2   # save it to a variable
    return result    # use it as output
my_function()
# that result is held in the code where the function has been called and we could save it as another variable.

# In this case, the output it's the result. 
# This value it's gonna be stored once the function is called. And it can be saved to another variable.
output = my_function()
print(f"The result is {output}")