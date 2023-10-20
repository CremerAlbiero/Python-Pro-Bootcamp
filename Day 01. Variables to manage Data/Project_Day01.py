#band name generator:

print("Welcome to the band name generator!")
city_name = input("Which city did you grew up in?\n")
pet_name = input("Insert an pet's name(Dog, Cat, Rat...\n")

city_name, pet_name = city_name.title(), pet_name.title()
print("Your band name could be:\n" + city_name + " " +pet_name +"'s")