import math

# Define the paint_calc function
def paint_calc(height, width, cover):
    cans_needed = math.ceil((height * width) / cover)
    print(f"You'll need {cans_needed} cans of paint.")

test_h = int(input("Height of wall (m): "))
test_w = int(input("Width of wall (m): "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)