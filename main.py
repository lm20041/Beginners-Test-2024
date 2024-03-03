my_dict = {
  "blue": "sky",
  "red": "fire",
  "green": "grass",
  "yellow": "sun",
  "purple": "grape",
  "orange": "orange",
  "black": "night",
  "white": "day",
}
to_find = input("Enter a colour: ")
# check if it's a key...
if to_find in my_dict:
  # get the value...
  coloured_object = my_dict[to_find]
  print(f"The colour {to_find} is {coloured_object}")
elif to_find in my_dict.values():
  print(f"{to_find} is a value in the dicionary")
else:
  print("Colour not found")

distance_dict = {
  "mm": 1000,
  "cm": 100,
  "m": 1,
  "km": 0.001,
}

# get amount and units (assume they are valid)
amount = float(input("how much? "))
from_unit = input("from unit? ")
to_unit = input("to unit? ")
# Multiply to get to our standard value...
multiply_by = distance_dict[from_unit]
standard = amount * multiply_by
# divide to get to our desired value...
divide_by = distance_dict[from_unit]
answer = standard / divide_by
print(f"{amount} {from_unit} is {answer} {to_unit}")