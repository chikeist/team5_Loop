import math

S = 0
x1 = float(input("Enter the x part of the coordinate: "))
y1 = float(input("Enter the y part of the coordinate: "))

while True:
    x2_input = input("Enter the x part of the coordinate (blank to quit): ")

    if x2_input == "":
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        S += distance
        break

    x2 = float(x2_input)
    y2 = float(input("Enter the y part of the coordinate: "))

    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    S += distance

    x1 = x2
    y1 = y2

print(f"The perimeter of that polygon is {S}")