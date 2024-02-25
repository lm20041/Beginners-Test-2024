# Ask the user for the width and height
# (assume they put in valid data)
def num_check(question):

  error = "Please enter a number that is more than 0\n"
  while True:
    try:
      #input
      response = float(input(question))
      #loop until they enter a number that is more than 0
      if response > 0:
        return response
      else:
        print(error)
    except ValueError:
      print("Please enter a number")
def calculate(width, height):
  area = width * height
  perimeter = (width * 2) + (height * 2)
  ans = f'the area is {area} and perimeter is {perimeter}'
  return ans
#main routine starts here...
keep_going = ""
while keep_going == "":
  # get width & height
  for item in range(0,1):
    width = num_check("Width: ")
  print()
  for item in range(0,1):
    height = num_check("Height: ")
  # calculate area/ perimeter
  # display output
  print(calculate(width, height))
  # ask user if they want to keep going
  keep_going = input("Press <enter> to keep going or any key to quit")
  print()