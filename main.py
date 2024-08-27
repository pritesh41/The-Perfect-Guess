import random

n=random.randint(1,100)
a=-1
guess= 0
while(a!=n):
    guess+= 1
    a= int(input("Guess Number: "))
    if a<n:
        print(f"it's lower the my choosed please increase your number: 🥱")
    elif a>n:
        print(f"it's higher then my choice please decrease your number: 🥱")
    elif a==n:
        print(f"\n\nyour choosed same number in {guess} guesses. \ncongrats You Won...!👏 \nSee you next time")
    elif a>100:
        print("please choose your number between 1 to 100")