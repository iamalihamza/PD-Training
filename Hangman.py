def insert_to_str(process_word, word, guess):
    process_word_list = list(process_word)  # This convert string into a list

    for index, value in enumerate(process_word_list):
        if guess == value:
            process_word_list[index] = '_'  # Adding _ in the specified index
            word[index] = guess

    return "".join(process_word_list)  # Again converting list into a string and returning it


def print_status_of_game(guess_count, word, used_letter):
    print(f"You have {guess_count} tries left.")
    print("Used Letters: ", ' '.join(used_letter))  # printing a list with no commas and brackets
    print("Word: ", ' '.join(word))


def guess_the_word(gw):
    gw = gw.lower()  # converting the guess word into lower case to avoid case-sensitive issues
    word_to_guess = process_word = gw
    guess_count = 6
    used_letter = []
    word = ['_' for _ in range(len(word_to_guess))]  # creating a list with '_' with same length as the word_to_guess
    print_status_of_game(guess_count, word, used_letter)

    while guess_count > 0:
        guess = str(input("Guess a letter: "))
        if len(guess) > 1:  # If user entered value has length more than 1 then he will re-enter the value
            print('Only enter single character')
            continue

        if guess in used_letter:  # if a character has entered before then ask user to enter again
            print("\nCharacter already used, enter another one")
            continue

        used_letter.append(guess)  # appending the user input character into used_letter list
        ind = process_word.find(guess)  # finding the user input value from guess word and returning the index of it

        if ind == -1:  # if user input is not in the guess_word then deduct the try count by 1
            guess_count -= 1
            print("\nWrong Character!!")
            print_status_of_game(guess_count, word, used_letter)
            continue

        process_word = insert_to_str(process_word, word, guess)  # adding _ in place of the value that matches
        # the user input
        print('\n')
        print_status_of_game(guess_count, word, used_letter)

        if word == list(word_to_guess):
            print(f"You guessed the word {''.join(word)}")
            break
    else:
        print("Better luck next time!!")


guess_word = "ferrari"
guess_the_word(guess_word)
