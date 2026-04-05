import random

words = ["attendes", "careing", "read", "write", "correct"]
word = random.choice(words)

guessed_letters = []

wrong_guesses = 0
max_guesses = 6

def display_word():
    display = ""
    for letter in word:

        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

print("🎮 Welcome to Hangman Game!")

while wrong_guesses < max_guesses:
    print("\nWord:", display_word())
    print("Wrong guesses left:", max_guesses - wrong_guesses)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter only ONE letter!")
        continue

    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        wrong_guesses += 1

    if all(letter in guessed_letters for letter in word):
        print("\n🎉 You WON! The word was:", word)
        break

if wrong_guesses == max_guesses:
    print("\n💀 Game Over! The word was:", word)