#transforming the input:
def format_name(first_name, last_name):
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()

    print(f"{formated_f_name} {formated_l_name}")

format_name("satoshi", "NAKAMOTO")



#Intead of printing, we could just return it as well.
def format_name2(first_name, last_name):
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()

    return f"{formated_f_name} {formated_l_name}"   #the MAIN DIFFERENCE is: the output REPLACES the code where the function was called.

#So we can save this new value in a variable.
formated_string = print(format_name2("satoshi", "NAKAMOTO"))



#An example is the len("str") function. It takes the value as the input, and then, uses 'return' and gives the final value.