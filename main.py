# functions go here
#======>      statement       <======
#main top image
def statement_generator(statement, decoration):
  print(f"\n{decoration * 5} {statement} {decoration * 5}")
#main bottom image
def statement_generator_end(statement_end, decoration):
  print(f"\n{decoration * 5} {statement_end} {decoration * 5}")
#main body image
def instructions():
  statement_generator("Instructions","-")
  
  print(f'''
Instructions go here.
- instruction 1 
- instruction 2 
- instruction 3 
- etc
  ''')
  statement_generator_end("END","-")
#======>       check         <======
def int_check(question, low):
  error = "Please enter a number that is more than 0\n"
  while True:
    try:
      #ask the uesr for a number
      response = int(input(question))
      # check that the number is more than zero
      if response > low:
        return response
      else:
        print(error)
    except ValueError:
      print(error)
#calculate the area / perimeter
def calculate(width, height):
  #image
  area = width * height
  perimeter = (width * 2) + (height * 2)
  ans_ImageFrame = f'the area of Image is {area} and perimeter is {perimeter}'
  return ans_ImageFrame
#======>  options: int, img, txt  <======
def get_filetype():
  while True:
    response = input("File type: ").lower()
  
    # check for 'i' or the exit code
    if response == "i" or response == "xxx":
      return response
    
    # check if it's an integer
    elif response in ['integer', 'int']:
      return "integer"
    # check for an image
    elif response in ['image', 'picture', 'img', 'p']:
      return "image"
    # check for an text
    elif response in ['text', 'txt']:
      return "text"
  
    # if the response is invalid output an error
    else:
      print("Please enter a valid file type")
#======>  Main routine goes here  <======
while True:
  file_type = get_filetype()
  # if user 'i', ask if they want an image / integer
  if file_type == "i":
    want_image = input("Press <enter> for an integer or any key for an image. ")
    if want_image == "":
      file_type = "integer"
    else:
      file_type= "image"
    break
  print(f"you chose {file_type}")

  # if integer
  if file_type == "integer":
    for item in range(0, 2):
      integer = int_check("Integer: ", 0)
      print(f"You chose {integer}")
  # if image Ask the user for the width and height
  if file_type == "image":
    for item in range(0, 2):
      height = int_check("Height: ", 0)
      print(f"You chose {height}")
    print()
    for item in range(0, 2):
      width = int_check("Width: ", 0)
      print(f"You chose {width}")
    calculate(width, height)
  # if text
  if file_type == "text":
    for item in range(0, 2):
      lines = int_check("lines: ", 0)
      print(f"You chose {lines}")
  if file_type == "xxx":
    break
# Display instructions if requested
want_instructions = input(f"Press <enter> to read the instructions or any key to continue: ").lower()

if want_instructions == "":
  instructions()

print("progrma continues")