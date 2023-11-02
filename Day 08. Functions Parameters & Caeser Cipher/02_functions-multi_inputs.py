#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?\n")

#Calling greet_with() with Positional Arguments. It's already received the value.
greet_with("Harry", "Nowhere")

#Calling greet_with() with Keyword Arguments
greet_with(name="Harry", location="Birmingham")    #I think that's more readable/clearer.
