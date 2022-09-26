import random

print('='*31)
print('Welcome to guess the number!!!')
print('='*31)

secret_number = random.randrange(1, 101)


for attempt in range(1, 4):
    print(f'Attempts: {attempt}/3')
    guess = int(input('Enter your guess to try to guess the secret number. "The range is from 1 to 100": '))
    if guess == secret_number:
        print('Congratulations! You have guessed the secret number.')
        print('End game!')
        break
    elif guess > secret_number:
        print('The secret number is smaller than your guess.')
    elif guess < secret_number:
        print('The secret number is highter than your guess.')
    if attempt == 3:
        print('Game over!!!')

