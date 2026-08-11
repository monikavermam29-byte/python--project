import random


easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "botter" , "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("welcome to the passwords guessing game")
print("choose a difficulty level: easy, medium, hard")

level = input('Enter your difficulty:').lower()
if level == 'easy':
     secret = random.choice(easy_words)

elif level == 'medium':
    secret =random.choice(medium_words)

elif level == 'hard':
    secret = random.choice(hard_words)

else:
    print("invalid choice.defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password")

while True:
    guess = input('Enter your guess:').lower()
    attempts += 1

    if guess == secret:
        print(f'congratulations! you guessed it in {attempts} attempts')
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[1]:
            hint += secret[i]
        else:
            hint += "_"

        print("Hint: ", hint)
    print("Gam over")
    