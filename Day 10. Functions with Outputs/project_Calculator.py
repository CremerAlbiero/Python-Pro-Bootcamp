def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def show_operations():
    for symbols in operations:
        print(symbols)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def check_operation(op):
    if op in operations:
        return print(f"{n1} {op} {n2} = {result}")
    else:
        return print("You didn't provide a valid operation.")

def operation(op, n1, n2):
    if op == '+':
        return add(n1, n2)
    elif op == '-':
        return subtract(n1, n2)
    elif op == "*":
        return multiply(n1, n2)
    elif op == "/":
        return divide(n1, n2)
    

n1 = int(input("Enter the 1st number: "))
show_operations()

op = input("Which operation do you want to do from above?\n")
n2 = int(input("Enter the 2nd number: "))

result = operation(op, n1, n2)
check_operation(op)


continue_calc = input("Do you want to continue with the result? Type 'yes' or 'no'\n")

if continue_calc == 'yes' or continue_calc == 'y':
    n3 = int(input("Enter the 3rd number: "))
    show_operations()
    op = input("Which operation do you want to do from above?\n")
    operation(op, result, n3)
    final_result = operation(op, result, n3)    #replacing the inputs in the function using the last output(return).

    print(f"{result} {op} {n3} = {final_result}")
    
else:
    final_result = result

print(f"""
     _____________________
    |  _________________  |
    |   {final_result}   
    |  _________________  |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
""")