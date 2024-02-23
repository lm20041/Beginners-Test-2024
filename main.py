#ask user for question
#
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

#main routine
for item in range(0,2):
  width = num_check("Width: ")
  print(width)

print()

for item in range(0,2):
  height = num_check("Height: ")
  print(height)