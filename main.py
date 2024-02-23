# Ask user for width and loop until they enter a number that is more than 0

error = "Please enter a number that is more than 0"
while True:
  try:
    #input
    width = float(input("Enter the width of the rectangle: "))
    #loop until they enter a number that is more than 0
    if width > 0:
      break
    else:
      print(error)
  except ValueError:
    print("Please enter a number")