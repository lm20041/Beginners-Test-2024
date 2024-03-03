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