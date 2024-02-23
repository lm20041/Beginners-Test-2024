#ask the user for their name
username = input("What is your name? ")

#ask the user for their favourite number (integer)
fav_num = int(input('what is your favourite number? '))
# doublec, halve and square the user's favourite number
double_num = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

#greet the user
print(f'Hello {username}, your favourite number is {fav_num}')
#output the results of doubling, halving and 
print(f'Double {fav_num} is {double_num}.')
print(f'Half {fav_num} is {halve}.')
print(f'Square {fav_num} is {square}.')
print()
print("Have a nice day.")
#squaring their favourite integer
