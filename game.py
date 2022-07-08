import random

print("-------------------------------")

print ("Welcome! Let's Play a Game :)")

print("-------------------------------")

user_choice = input("Rock, Paper, or Scissors? ")

print("-------------------------------")

random_num = random.randint(0,2)
if random_num == 0:
    cpu_choice = "Rock"
elif random_num == 1:
    cpu_choice = "Paper"
elif random_num == 2:
    cpu_choice = "Scissors"

print("Your Choice:", user_choice)

print("Computer Chouce:", cpu_choice)

print("-------------------------------")

