import random

user = int(input("Enter a number: "))
numbers_at_random =  random.randrange(1,100)

while(1):
    try:
        if user == numbers_at_random:
            print("Correct no \n Congrats on your first try")
        elif (numbers_at_random > 25 and numbers_at_random < 50):
                user = int(input("The number is below 50, try again: "))
                if user == numbers_at_random:
                    print("correct no")
        elif (numbers_at_random > 50 and numbers_at_random < 75):
                user = int(input("The number is above 50, try again: "))
                if user == numbers_at_random:
                    print("correct no")
        elif (numbers_at_random < 25):
                user = int(input("The number is below 25, try again: "))
                if user == numbers_at_random:
                    print("correct no")
        elif (numbers_at_random > 75):
                user = int(input("The number is above 75, try again: "))
                if user == numbers_at_random:
                    print("correct no")
        break

    except :
        print("Something went wrong")
    
    finally:
        print("you won the game HURRAY!!!!!")