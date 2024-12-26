import random

num=random.randint(1,20)
guess=int(input("Guess the numer that im thinking 1 to 20 : "))
attempt=1
while num!=guess and attempt<=4:
    if guess>num:
        print("your guess is higher")
    else:
        print("your guess is lower")
    attempt+=1
    guess=int(input("Guess the another numer 1 to 20 : "))

if num==guess:
    print("You won!!")
else:
    print("You Lost, please try again")



