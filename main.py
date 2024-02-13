#Ask the user for the width and height
# (assume they put  in vaild data)
def calculate_area_perimeter():
  global width
  global height
  while True:
    try:
      width = float(input("Enter the width: "))
      height = float(input("Enter the height: "))
      if width > 0 and height > 0:
        return
      else:
        print("Please enter a valid number")
    except ValueError:
      print("Please enter a valid number")
calculate_area_perimeter()
#calculate the area / perimeter
area = width * height
perimeter = 2 * (width + height)
#output the area and perimeter
print("The area is", width,"in width" , height,"in height")
print("The perimeter is", perimeter)

#-------------------------------------#