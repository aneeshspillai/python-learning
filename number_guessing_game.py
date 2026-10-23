secret_number = 7
guess = int(input("Guess the number: "))
attempt = 1
while guess != secret_number:
    if attempt == 3:
        print("Game over! The number was", secret_number)
        break
    attempt += 1
    guess = int(input("Guess again: "))
else:
    print("Correct! You won!")