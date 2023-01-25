import random

'''
#User guess computer's number

def guess(x):
    random_no = random.randint(1,x)
    guess = 0
    while guess != random_no:
        guess = int(input(f'Guess a  number between 1 and {x}: '))
        
        if guess < random_no:
            print("Sorry, guess again. Too Low")
        elif guess > random_no:
            print("Sorry, guess again. Too high")
        
    print(f"Yay, congrats. You have guess the number {random_no} correctly!!")

guess(10)

'''

#Computer guess user's number
def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != 'c' :
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer guessed your number {guess} correctly!!")

computer_guess(10)

