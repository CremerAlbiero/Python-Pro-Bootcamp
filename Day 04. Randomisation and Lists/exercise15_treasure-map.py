line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot (using letter/number system, like A3).")
position = input("Where do you want to put the treasure? ")
# Don't change the code above

if len(position) != 2 or position[0].lower() not in ['a', 'b', 'c'] or position[1] not in ['1', '2', '3']:
    print("Invalid input. Please use just A1, B2, etc.")
else:
    row = int(position[1]) - 1  
    col = ord(position[0].lower()) - ord('a')
    map[row][col] = "[X]"

print(f"{line1}\n{line2}\n{line3}")