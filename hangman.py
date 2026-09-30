import random
words = ["technology", "intelligent", "automation", "engineer", "processor"]
word = random.choice(words)
guessed_letters = []
max_wrong = 6
wrong_guesses = 0
print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.\n")
while wrong_guesses < max_wrong:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word!")
        print("The word was:", word)
        break
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses left:", max_wrong - wrong_guesses)
        print()
if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("The correct word was:", word)