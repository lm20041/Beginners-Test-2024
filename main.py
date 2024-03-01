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

#Main Routine goes here
text_ans = calc_text_bits()
print(text_ans)
print()
image_ans = image_calc()
print(image_ans)