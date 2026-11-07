clues = ["It's a two-digit number.", "It's greater than 40.", "It's less than 50.", "It's an even number."]
clues_1 = int(input("Do you want a clue? (1 for yes, 0 for no): "))
if clues_1 == 1:
    for clue in clues:
        print(clue)

secret_number = 46
lives = 5

while lives > 0:
    t = int(input("guess the number: "))

    if t == secret_number:
        print("Congratulations! You guessed the number.")
        break
    else:
        lives -= 1
        print("Sorry, you didn't guess the number.")
        if lives > 0:
            print(f"You have {lives} lives left.")
        else:
            print("Game over. You ran out of lives.")

