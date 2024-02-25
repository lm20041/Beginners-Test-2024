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
def calculate(width, height, cost):
  area = width * height
  perimeter = (width * 2) + (height * 2)
  total_cost = perimeter * cost
  return area, perimeter, total_cost  
def output(area, perimeter, total_cost):
  ans1 = f'the area is {area}'
  ans2 = f'the perimeter is {perimeter}'
  ans3 = f'the total_cost is {total_cost}'
  return ans1, ans2, ans3
#main routine starts here...
keep_going = ""
while keep_going == "":
  # get width, height & cost
  for item in range(0,1):
    width = num_check("Width: ")
  print()
  for item in range(0,1):
    height = num_check("Height: ")
  print()
  for item in range(0,1):
    cost = num_check("Cost per unit: ")
  # calculate area/ perimeter
  area, perimeter, total_cost = calculate(width, height, cost)
  # display output
  print()
  ans1, ans2, ans3 = output(area, perimeter, total_cost)
  print(ans1)
  print(ans2)
  print(ans3)
  # ask user if they want to keep going
  keep_going = input("Press <enter> to keep going or any key to quit")
  print()
  
print(f'Thank you for using the program')