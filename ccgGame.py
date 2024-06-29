import random

continue_playing = True
colors = ["Red", "Yellow", "Green", "Blue"]



while continue_playing:
    value = random.randint(1, 4)

    while True:
        try:
            user_color_choice = int(input("What color do you choose? \nRed:1\nYellow:2\nGreen:3\nBlue:4\n"))
            if 1 <= user_color_choice <= 4:
                break
            else:
                print("Please enter a valid integer ")
        except ValueError:
            print("Please enter a valid integer ")

    if value != user_color_choice:
        user_color = colors[user_color_choice - 1]
        print(f"You chose {user_color}")
        computer_color = colors[value - 1]
        print(f"The computer chose {computer_color}")
        print("Sorry you lost")
        while True:
            user_continue_choice = input("Do you want to continue playing? (Y/N)\n").capitalize().strip()
            if user_continue_choice == "Y":
                continue_playing = True
                break
            elif user_continue_choice == "N":
                continue_playing = False
                break
            else:
                print("Please enter a valid response")
    else:
        user_color = colors[user_color_choice - 1]
        print(f"You chose {user_color}")
        computer_color = colors[value - 1]
        print(f"The computer chose {computer_color}")
        print("Congrats, you won!")
        continue_playing = False




