import random

choices = {
    0: "Rock",
    1: "Scissors",
    2: "Paper"
}

def check(comp, user):
    if comp == user:
        return 0
    if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1
    return 1

while True:
    comp = random.randint(0, 2)

    user = int(input("0 for Rock, 1 for Scissors, and 2 for Paper: "))

    if user not in choices:
        print("Invalid choice.\nPlease type 0 for Rock, 1 for Scissors, or 2 for Paper.")
        continue

    print("You chose:", choices[user])
    print("Computer chose:", choices[comp])
    result = check(comp, user)

    if result == 0:
        print("It's a draw!")
    elif result == -1:
        print("You lose!")
    else:
        print("You win!")

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again != 'Y':
        print("Thanks for playing. Goodbye!")
        break