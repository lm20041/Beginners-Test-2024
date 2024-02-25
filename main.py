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

# Main routine goes here

# Display instructions if requested
want_instructions = input(f"Press <enter> to read the instructions or any key to continue: ").lower()

if want_instructions == "":
  instructions()

print("progrma continues")