import random

colors = ["Red", "Yellow", "Green", "Blue"]

while True:
    user_color_choice = None
    while user_color_choice not in range(1, 5):
        try:
            user_color_choice = int(input("What color do you choose? \nRed:1\nYellow:2\nGreen:3\nBlue:4\n"))
        except ValueError:
            print("Please enter a valid integer")

    user_color = colors[user_color_choice - 1]
    computer_color = random.choice(colors)

    print(f"You chose {user_color}")
    print(f"The computer chose {computer_color}")

    if user_color == computer_color:
        print("Congrats, you won!")
    else:
        print("Sorry you lost")

    user_continue_choice = input("Do you want to continue playing? (Y/N)\n").capitalize().strip()
    if user_continue_choice != "Y":
        break
