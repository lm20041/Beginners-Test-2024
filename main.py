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

#calculate the area / perimeter
def calculate(width, height):
  area = width * height
  perimeter = (width * 2) + (height * 2)
  ans = f'the area is {area} and perimeter is {perimeter}'
  return ans
#Input the area and perimeter
for item in range(0,1):
  width = num_check("Width: ")

print()

for item in range(0,1):
  height = num_check("Height: ")
#Output the area and perimeter
print(calculate(width, height))