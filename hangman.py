import random


def open_game():
    print('=' * 22)
    print('Welcome to Hangman!!!')
    print('=' * 22)


def word():
    file = open('words.txt', 'r')
    words = []
    for word in file:
        words.append(word.strip().lower())
    file.close()
    return words[random.randrange(0, len(words))]


def draw_gallows(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def game():
    open_game()
    secret_word = word()
    letters = ['_' for letter in secret_word]
    hanged = False
    hit = False
    mistakes = 0

    while (not hit and not hanged):
        print(letters)
        kick = input('One letter?')
        kick = kick.strip().lower()

        if kick in secret_word:
            index = 0
            for letter in secret_word:
                if kick == letter:
                    letters[index] = kick
                index += 1
        else:
            mistakes += 1
            draw_gallows(mistakes)

        hanged = mistakes == 7
        hit = '_' not in letters
        # if mistakes == 6 or '_' not in letters:
        #     break

    if '_' not in letters:
        print(letters)
        print('Congratulation, you have won!')
    else:
        print('Game over!')


if __name__ == '__main__':
    game()
