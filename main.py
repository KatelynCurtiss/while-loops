# Katelyn Curtiss
# 6 December 2024
# While Loops


# import random

# name = input("Hello what is your name? ")
# number = random.randint(1, 100)
# print("Hi " + name + ", im thinking of a number between 1 and 100. ")
# guessestaken = 0

# while guessestaken < 5:
#     guess = input("Enter a guess!: ")
#     guess = int(guess)
#     if guess < number:
#         print("That was too low")
#     elif guess > number:
#         print("that was too high!")
#     else:
#         break

# if guess == number:
#     print("Winner winner, chicken dinner! congrats " + name + " u guessed the correct number")
# else:
#     print("you lose, too bad. better luck next time. The right number was", number)





# Tempature 
#     name = input("Hello what is your name? ")
# number = random.randint(1, 100)
# print("Hi " + name + ". ")
# guessestaken = 0

# while guessestaken < 5:
#     guess = input("Enter a tempature in degrees Fahrenheit (-9999 to quit) !: ")
#     guess = int(guess)
#     if guess < number:
#         print("That was too low")
#     elif guess > number:
#         print("that was too high!")
#     else:
#         break

# if guess == number:
#     print("")
# else:
#     print("you lose, too bad. better luck next time. The right number was", number)

temperatures = []

keep_looping = True
while keep_looping:
    temperature = int(input('Please enter a Fahrenheit temperature (or -9999 to quit):\n'))

    if temperature == -9999:
        keep_looping = False
    else:
        temperatures.append(temperature)

if len(temperatures) > 0:
    print(f"Temperatures entered: {temperatures}")
    print(f"Average temperature: {sum(temperatures)/len(temperatures)}")


