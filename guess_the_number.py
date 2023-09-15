import random
n = random.randint(1, 100)
number_of_guesses = 1
print("Number of guesses is limited to only 9 times")
while number_of_guesses <= 6:
    guessed_number = int(input("Guess the number between 0 to 100 : "))
    if guessed_number < n:
        print("You entered Smaller Number... Please input Larger NUmber")
    elif guessed_number > n:
        print("You entered Larger Number... Please input Smaller Number")
    else:
        print("GREAT! ___YOU WON THE GAME___")
        print("Number of guesses you took to finish : ", number_of_guesses)
        break
    print("Number of guesses left : ", 9 - number_of_guesses)
    number_of_guesses = number_of_guesses + 1

if number_of_guesses > 9:
    print("Game Over!")
