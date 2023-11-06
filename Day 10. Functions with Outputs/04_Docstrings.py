# It's possible to add a little documentation in the function when it is called.
# Example:

def format_name(f_name, l_name):
    """Take a first and last name and format it
    as a title version."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs." 
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"  

#It'll show when you write it.
format_name("vitalik", "BUTERIN")