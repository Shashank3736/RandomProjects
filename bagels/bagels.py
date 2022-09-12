import random 

NUM_DIGITS = 3
MAX_GUESSES = 10
CLUES = ('Pico', 'Fermi', 'Bagels', 'True')

def main():
    print("""Bagels, a detective logic game. Made by Shreyash Raj.

    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is here are some clues.

    When I say:     That means:
        Pico         One digit is correct but in the wrong position.
        Fermi        One digit is correct and in the right position.
        Bagels       No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.""".format(NUM_DIGITS))

    while True:
        secret_num = get_secret_num()
        print("I have thought of a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        result = False

        for i in range(MAX_GUESSES):
            guess: str = input(f"Guess #{i+1}: ")
            clue = get_clues(guess, secret_num)

            if clue == CLUES[3]:
                result = True
                break
            else:
                print(clue)
        
        if result:
            print('You got it.')
        else:
            print("You have already used all your guesses. The correct answer is {}.".format(secret_num))
        
        print('Do you want to play again? (Yes/No)')
        next_game: str = input()

        if next_game.lower() == 'no':
            print("Thanks for playing the game.")
            break
        else:
            print("Ok! Let's continue the game to next round.")


def get_secret_num() -> str:
    """Returns a unique number."""

    numbers = list('1234567890')
    random.shuffle(numbers)

    secret_num = ''

    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])

    return secret_num

def get_clues(guess: str, secret_num: str) -> str:
    if guess == secret_num:
        return CLUES[3]
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append(CLUES[1])
        elif guess[i] in secret_num:
            clues.append(CLUES[0])
        
    if len(clues) == 0:
        return CLUES[2]
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
