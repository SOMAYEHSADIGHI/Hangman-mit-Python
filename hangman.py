import random

# 1) list of name
# 2) select one name randomly
# 3) get user char
# 4) check => show feedback
# 5) guess >0 => win/loss

names = ["Ali", "Max", "Anton", "Sara", "Samaneh", "Somayeh", "Maria"]


selected_name = random.choice(names).lower()


guess_count = len(selected_name)
guessed_list = ["-"] * len(selected_name)

current_guess = " ".join(guessed_list)
print(current_guess)

while guess_count > 0:
    guessed_char = input("Enter a char: \n")

    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print("You have guessed befor, try new character")
            else:
                for idx, char in enumerate(selected_name):
                    if char == guessed_char:
                        guessed_list[idx] = guessed_char
                current_guess = " ".join(guessed_list)
                print(f"Perfect => {current_guess}")

                if not " ".join(guessed_list):
                    print("You won!")
                    break

        else:
            guess_count -= 1
            print("Wrong! => remained guesses:{guess_count}")
    else:
        print("Please enter a valid character")
