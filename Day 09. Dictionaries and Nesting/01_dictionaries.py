#Key and Value. Like an word, and the definition of it.

dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary by its key:
print(dictionary["Bug"])

# Adding new items to dictionary:
dictionary["Loop"] = "The action of doing something over and over again."
print(dictionary)

# create an empty dictionary
empty_dictionary = {}

# Edit and item in a dictionary
dictionary["Bug"] = "A mistake or problem in a computer program."
print(dictionary)

#Loop through a dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])