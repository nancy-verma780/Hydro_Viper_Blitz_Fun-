'''
1 for snake
-1 for water
0 for gun
'''
import random
print("Welcome to Snake, Water, Gun game!")
user_score = 0
computer_score = 0
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

# Buy now we have 2 number (variables), you and computer

print(f"You chose {reverseDict[you]}")

if(computer == you):
    print("Draw!")

else:
    if(computer == -1 and you == 1):
     print("You win!")
        user_score +=1
     print("Computer chose water")

    elif(computer == -1 and you == 0):
      print("You lose!")
        computer_score += 1
      print("Computer chose water")

    elif(computer == 1 and you == 0):
      print("You win!")
        user_score +=1

      print("Computer chose snake")

    elif(computer == 1 and you == -1):
      print("You lose!")
        computer_score += 1

      print("Computer chose snake")

    elif(computer == 0 and you == 1):
      print("You lose!")
        computer_score += 1

      print("Computer chose Gun")

    elif(computer == 0 and you == -1):
      print("You win!")
        user_score +=1

      print("Computer chose Gun")

    else:
      print("Something went wrong")

print(f"\nScore:")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")
