#Functions has to be used with some specific data types. like "len", for strings. Otherwise, it'll get an error.
num_char = len(input("Whats your Name?\n"))
print(type(num_char))
#when you're not sure about the datatype, you can simply use type()

#convert data:
new_num_char = str(num_char)

print("Your name has "+ new_num_char + " characters")

a = float(123)
print(type(a))

print(70 + float("100.5"))
#this will print 170.5. Behind the scenes, it's converting the string "100.5" into a floating-point number and then adding 70 to a 100.5.

print(str(70) + str(100))