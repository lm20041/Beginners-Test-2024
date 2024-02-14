#@ [Ask the user for width, length and loop until they enter a number more then zero]
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
  # [get width, length, cost]
  width = num_check("width: ")
  length = num_check("length: ")
  cost = num_check("cost: ")
  # [calculate]
  perimeter= (width + length) * 2
  total_cost = perimeter * cost
  
  # [Display output]
  print("perimeter is:", perimeter, "in units")
  print("cost is:", cost,"for each unit")
  print("total cost is: ${:.2f}".format(total_cost))
  
  # [ask if user wants to continue]
  keep_going = input("Press <enter> to keep going or any key to quit")
  print()