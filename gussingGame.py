secret = 7
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input('Guess the number: '))
    if guess == secret:
        print(f'You guessed the correct number! It is {secret}')
        break
    else:
        guess_count += 1
        print('Wrong')
        print(str(guess_limit - guess_count) + ' Guesses left')
else:
    print("Sorry, you didn't guess my number")
print('DONE')