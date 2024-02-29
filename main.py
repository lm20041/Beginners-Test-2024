# functions go here
#main top image
def statement_generator(statement, decoration):
  print(f"\n{decoration * 5} {statement} {decoration * 5}")
#main bottom image
def statement_generator_end(statement_end, decoration):
  print(f"\n{decoration * 5} {statement_end} {decoration * 5}")
#main body image
def instructions():
  statement_generator("Instructions","-")
  
  print('''
Instructions go here.
- instruction 1
- instruction 2
- instruction 3
- etc
  ''')
  
  statement_generator_end("END","-")
#
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
  
# Main routine goes here
while True:
  file_type = get_filetype()
  # if user 'i', ask if they want an image / integer
  if file_type == "i":
    want_image = input("Press <enter> for an integer or any key for an image. ")
    if want_image == "":
      file_type = "integer"
    else:
      file_type = "image"
    break
  print(f"you chose {file_type}")

  if file_type == "xxx":
    break
# Display instructions if requested
want_instructions = input(f"Press <enter> to read the instructions or any key to continue: ").lower()

if want_instructions == "":
  instructions()

print("progrma continues")