import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'peach', 'pear']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect guess!")
            attempts -= 1
            if attempts == 0:
                print("Sorry, you ran out of attempts. The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations, you guessed the word:", word)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    hangman()
