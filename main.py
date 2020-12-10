rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

user = input(f"Please type 0 for Rock, 1 for Paper, or 2 for Scissors.")

print(f"\nYou choose:")

if user == 0:
	print(rock)
elif user == 1:
	print(paper)
else:
	print(scissors)

print(f"Computer chooses:")

computer = random.randint(0,2)

if computer == 0:
	print(rock)
	if user == 0:
		print(f"Tie!")
	elif user == 1:
		print(f"You win!")
	else:
		print(f"You lose.")

elif computer == 1:
	print(paper)
	if user == 0:
		print(f"You lose.")
	elif user == 1:
		print(f"Tie")
	else:
		print(f"You win!")

else:
	print(scissors)
	if user == 0:
		print(f"You win!")
	elif user == 1:
		print(f"You lose.")
	else:
		print(f"Tie")

