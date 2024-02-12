# ask the user for width and loop until they
# enter a number that is more than zero
error = "Invalid, please enter a valid"
while True:

    try:
        #ask the user for width
        width = float(int(input("Enter the width: ")))
        #check that the number is more than zero
        if width > 0:
          break
        else:
          print(error, "input")
    except ValueError:
        print(error, "input")