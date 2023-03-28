import random

words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "grape", "pear", "peach", "plum"]

word = random.choice(words)

max_guesses = 10

guessed_letters = set()

incorrect_guesses = 0

current_word = "_" * len(word)

print("Welcome to Hangman!")
print("The word has", len(word), "letters.")
print(current_word)

while incorrect_guesses < max_guesses and "_" in current_word:
    guess = input("Guess a letter: ")
    
    if guess.isalpha() and guess not in guessed_letters:
        guessed_letters.add(guess)
        
        if guess in word:
            current_word = "".join([guess if letter == guess else current_word[i] for i, letter in enumerate(word)])
            
            print(current_word)
        else:
            incorrect_guesses += 1
            
            print("Sorry, that letter is not in the word.")
            print("You have", max_guesses - incorrect_guesses, "guesses left.")
    else:
        print("Invalid guess. Please enter a letter you haven't already guessed.")
        
if "_" not in current_word:
    print("Congratulations, you guessed the word!")
else:
    print("Sorry, you ran out of guesses. The word was", word)
