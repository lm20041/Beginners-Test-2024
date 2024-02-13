# Ask the user for width and height
# and loop until they enter a number 
# more then zero
def num_check(question):
  error = "Please enter a number that is more then zero"
  while True:
    try:
      #ask the user for a number
      response = float(input(question))
      
      #check that the number is more then zero
      if response > 0:
        return response
      else:
        print(error)
    except ValueError:
      print(error)
      
# main routine staring here...
keep_going = ""
while keep_going == "":
  # get width and height
  width = num_check("width: ")
  height = num_check("height: ")

  # calculate area / perimeter
  area = width * height
  perimeter = (width + height) * 2
  
  # Display output
  print("perimeter:", perimeter, "units")
  print("area:", area, "square units")
  
  # ask if user wants to continue
  keep_going = input("Press <enter> to keep going or any key to quit")
  print()