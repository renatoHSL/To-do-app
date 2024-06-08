from experiments.coding_exercise_feet.Converters14 import convert
from experiments.coding_exercise_feet.Parses14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")

else:
    print("Kid can use the slide.")
