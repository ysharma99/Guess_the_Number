import random 

def guess (x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} "))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. Too high")
    print (f"Yayy congrats you guessed {random_number} correctly")

def computer_guess(x):
    low = 1 
    high = x
    feedback = '' 
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could also be high because low=high
        guess= random.randint(low, high)
        feedback = input(f"is {guess} to low (l) or high (h) or correct? (c) ").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback =='l':
            low = guess + 1
    print(f'yay! the computer guesed your number, {guess} correctly!')

computer_guess(10)







#guess(10)
