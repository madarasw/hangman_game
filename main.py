import random
import time
import hangman_art
import word_list

print(hangman_art.logo)

word_list = word_list.word_list
word = word_list[random.randint(0, len(word_list) - 1)]
word_length = len(word)
word_to_guess = []
entered = []
life = 7
end = False


def print_word_with_space(list_in):
    """"
    input: list
    return: none
    Functionality: This function will print the items in a given list with spaces inbetween
    """

    word_in = ""
    for letter_ in list_in:
        word_in += letter_ + " "
    print("\n" + word_in + "\n")


# Create initial empty array to hold the word
for e in range(word_length):
    word_to_guess.append("_")

# Greetings
print("\nWelcome to Hangman... \n\nGuess the below word")
print_word_with_space(word_to_guess)

# Game runs until the all the letters in the word is guessed or
# the user run out of all the chances
while not end:
    letter = input("\nPlease enter guessed letter: ").lower()
    if letter in entered:
        print("\n\n You have already entered that letter.\n")
        print("\n******************************************\n")

    elif letter in word:
        print("That's correct...!")
        for letter_ in range(0, word_length):
            if word[letter_] == letter:
                word_to_guess[letter_] = letter
        print_word_with_space(word_to_guess)
        print("\n******************************************\n")
        if "_" not in word_to_guess:
            print("You win...!\n")
            end = True
            time.sleep(5)

    else:
        life -= 1
        print(hangman_art.stages[(life - 7)])
        print_word_with_space(word_to_guess)
        if life == 0:
            print("\nYou lose...!\n\ncorrect word is " + word)
            end = True
            time.sleep(5)
        else:
            print("Wrong guess, One life is gone")
            print("\n******************************************\n")

    entered.append(letter)
