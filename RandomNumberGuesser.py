import random

n = random.randint (1,314)
print("I am thinking of a number between 1 and 314")

running = True
while running:
        guess_str = input("Take a guess! ")
        guess = int(guess_str)
        if guess == n:
            print("Well done! That is correct!")
            running = False
        elif guess < n:
            print("Try a larger number")
        else:
            print("Try a smaller number")
                
