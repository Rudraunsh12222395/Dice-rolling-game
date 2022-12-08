import random
user_score = 0
dice_score = 0
while True:
    user = 0
    while not int(user) in range(1,7):
        user = int(input("Enter the dice Number: "))
    dice = random.randint(1,6)
    if user == dice:
        user_score += 1
        print("you won, User scores")
    else:
        dice_score += 1
        print("you lose, computer scores")

    again = str(input("try again? (Y/N): "))
    if again == "N":
        break

print("user: ", user_score)
print("dice: ", dice_score)