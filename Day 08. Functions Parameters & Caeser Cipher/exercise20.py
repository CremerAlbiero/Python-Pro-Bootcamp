from math import ceil

# math.ceil will round the number up. For example, you can't buy 4.1 cans of paint, so you should buy 5 cans.
def paint_calc(height, width, cover):
    cans_needed = ceil((height * width) / cover)
    print(f"You'll need {cans_needed} cans of paint.")

# Input for wall height and width
user_h = int(input("Height of wall (m): "))
user_w = int(input("Width of wall (m): "))
coverage = 5

# Calling the function.
paint_calc(height=user_h, width=user_w, cover=coverage)