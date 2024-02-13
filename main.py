# ask the user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Invalid, please enter a valid"
    while True:
    
        try:
            #ask the user for width
            response = float(input("Enter the " + question + ": "))
            #check that the number is more than zero
            if response > 0:
              return response
            else:
              print(error, "input")
        except ValueError:
            print(error, "input")

# main routine goes here
for item in range(0, 2):
    width = num_check("Width")
    print(width)

for item in range(0, 2):
    height = num_check("Height")
    print(height)