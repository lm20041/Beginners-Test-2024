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
#======>    Calculates      <======
#Calculates how many bits are needed to represent an integer
def image_calc():
  # get the image dimensions
  width = int_check("Width: ", 0)
  height = int_check("Height: ", 0)

  # calculate the number of pixels and multiply by 24 to get the number of bits
  num_pixels = width * height
  num_bits = num_pixels * 24

  # set up answer and return it
  answer = (f"Number of pixels: {width} X {height} = {num_pixels}" 
    f"\nNumber of bits {num_pixels} X 24 ={num_bits}")
  return answer
#Calculates how many bits are needed to represent an integer
def integer_calc():
  # get the image dimensions
  integer = int_check("Integer: ", 0)
  # convert the integer to binary and work out the number of bits needed
  raw_binary = bin(integer)
  # remove the 0b from the front of the raw_binary
  binary = raw_binary[2:]
  num_bits = len(binary) 
  # set up answer and return it
  answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."
  return answer
#Calculates number of bits needed to represent text in ascii
def calc_text_bits():
  #get text from user
  response = input("Enter text to calculate bits: ")
  #calculate number of bits
  num_chars = len(response)
  num_bits = num_chars * 8
  # set up answer and return it
  answer = (f"{response} has {num_chars} characters." 
  f"\nwe need {num_chars} X 8 bits to represent it"
  f"\nwhich is {num_bits} bits")
  return answer

#======>      options:      <======
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
  if file_type == "xxx":
    break
  # if user 'i', ask if they want an image / integer
  if file_type == "i":
    want_image = input("Press <enter> for an integer or any key for an image. ")
    if want_image == "":
      file_type = "integer"
    else:
      file_type= "image"
    break
  print(f"you chose {file_type}")
  try:
    # if integer
    if file_type == "integer":
      integer_ans = integer_calc()
      print(integer_ans)
    # if image Ask the user for the width and height
    elif file_type == "image":
      image_ans = image_calc()
      print(image_ans)
    # if text
    else:
      text_bits_ans = calc_text_bits()
      print(text_bits_ans)
  except ValueError:
    print("Please enter a valid file type")


# Display instructions if requested
want_instructions = input(f"Press <enter> to read the instructions or any key to continue: ").lower()

if want_instructions == "":
  instructions()
print("progrma continues")