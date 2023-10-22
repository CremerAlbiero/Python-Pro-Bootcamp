#round
print(round(8 / 3))

#round: you can specify the number of digits of precision you want to round it to.
print(round(8 / 3, 2))   #2.67 result

# // (show the result as integer)  <class 'int'>. If use / the result will be a floating number.
print(8 // 3)   #3 result <class 'int'>.


#continue performing calculations
result = 4 / 2
result /= 2
print(result)

#short += /= ("take the previous value and add to it").
score = 0
score += 1

print(f"You score is {score}")
#f-String can combine a lot of data and data types.