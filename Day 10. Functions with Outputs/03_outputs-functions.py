def format_name2(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."  #this is going to escape the function. And it prints 'None' by default.
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"  


formated_string = print(format_name2("satoshi", "NAKAMOTO"))
