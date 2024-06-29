from hangman_life import game_name, lives
print(game_name)

answer = 'python'
characters = list(answer)
print(f"Number of letters in the word: {len(characters)}")
attempt = 7
winning_num = 0
tried_list = []

while attempt > 0 and winning_num != len(characters):
    print(f"Attempts: {attempt}")
    user_letter = input("What letter do you choose?\n").strip().lower()

    if user_letter == answer:
        winning_num = len(characters)
    elif user_letter in tried_list:
        print("You already guessed this letter")
    elif user_letter in characters:
        while True:
            try:
                check_index = characters.index(user_letter)
                characters[check_index] = " "
                tried_list.append(user_letter)
                print(f"{user_letter} is the {check_index + 1} letter")
                winning_num += 1
            except ValueError:
                break
    else:
        attempt -= 1
        tried_list.append(user_letter)
        print(lives[attempt])
        print(f"{user_letter} is not in the word")

if attempt == 0:
    print(f"You lost\n The word is {answer}")

if winning_num == len(characters):
    print(f"You won\nThe word is {answer}")
