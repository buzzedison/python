
# i = 0
# while i < 20:
# print(i)
# i = i + 1


# print('x' * 10)

# name = input('What is your name? ')
# age = input('How old are you? ')

# print('My name is ' + name + 'and i am ' + age + 'years old ')


# Calculate how old i am

# name = input('type in your name: ')
# birth_date = input('what year were you born? ')
# current_date = input('what year are we in currently? ')
# age = int(current_date) - int(birth_date)
# print(age)

# Calculate how many litres of juice from Gallons

# gallons = input("How many Gallons? ")
# litres = int(gallons) * 8
# print(litres)
# print('litres')

# Multiline strings
# me = """who am i
# what can i do
# where am i going """


# print(me)
# store = "How many fruits do you have in the store"
# print(store[0:])

# print Donald [Trump] loves python. classwork //Formating strings
# first_name = "Donald"
# last_name = "Trump"
# president = f"{first_name} [{last_name}] loves python"
# print(president)

# string methods
#store = "We have many fruits here"
# print(store.upper()) #prints strings in capital letters
#print(store.replace('We', 'Us'))
# print(store.find('have'))
# print(store.find('f'))
# print(len(store))

# performing math functions
import math
#price = 7.5
# print(math.ceil(price))
# print(math.floor(price))
# print(math.fabs(price)) //absolute value of the number

#print(f'The value of pie is  {math.pi}')
# Declare a price variable, give a discount of 10%, find the new price for the customer, and print result.
#price = 7.5
#discount = 10/100 * 7.5
#new_price = price - discount
# print(new_price)
#print(math.pow(2, 3))

# print random numbers from a set
#from random import randrange
#price = randrange(0, 20)

# print(price)

# if statements // Guess the random number
#from random import randrange
#guess = input('guess the number: ')
#guess_range = randrange(0, 100)
# if guess == guess_range:
#  print('You Won!')
# else:
#print("Try again")
# print(guess_range)

# classwork find the down payment of a house. 10% or 20% downpayment
#house = input('What is the cost of the house you are buying: ')
#income = input("What is your monthly salary: ")
#housea = 0.20 * int(house)
#houseb = 0.35 * int(house)
#average = 5000

# if income == average:
# print(housea)
# else:
#  print(houseb)

# use if statement to ask the user for their name but cannot be less than 3 characters or more than 50
#name = input('what is your name: ')
# if len(name) < 3:
# print("Name must be at least three characters long")
# elif len(name) > 50:
#print("Name cannot be more than 50 characters ")
# else:
# print("Congratulations!, your name looks good")
# print(name)

# python while loops
#x = 1
# while x <= 10:
#  print(x)
#   x += 1
# print('success')

#guessing game
guess_secret = 13
guess_count = 0
guess_limit = 3

while guess_count <= guess_limit:
    guess = int(input("Enter a guess: "))
    guess_count +=1
    if guess == guess_secret:
            print ("Yes, you won! ****")
            break
    else:
        print("please try again")
else:
    print("Game Over!!! ")


