# hangman(mini version)

word = "python"
guessed = ""

while True:
    display = ""
    for ch in word:
        display += ch if ch in guessed else "_"

    print(display)

    if display == word:
        print("🎉 You guessed the word!")
        break

    guess = input("Guess a letter: ")
    guessed += guess
