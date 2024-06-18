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
game_img=[rock,paper,scissors]
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice>=3 or choice<0:
  print("You entered a invalid number")
else:
  print(game_img[choice])
  print("Computer Choose:")
  Computer_choice=random.randint(0,2)
  print(game_img[Computer_choice])
  if choice==0 and Computer_choice==2:
    print("You win!!")
  elif Computer_choice==0 and choice==2:
    print("You loose!!")
  elif Computer_choice>choice:
    print("You loose!!")
  elif choice> Computer_choice:
    print("You win!!")
  elif Computer_choice==choice:
    print("Draw!!")
    
 