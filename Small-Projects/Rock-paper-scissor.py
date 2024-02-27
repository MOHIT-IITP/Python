# rock paper and scissor game 
import random
game = random.randint(0, 2)
choice = int(input('What do you choose? type 0 for Rock , 1 for Paper and 2 for Scissor. '))
print("
██████╗  ██████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗     ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗     
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗    
██████╔╝██║   ██║██║     █████╔╝     ██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝    ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝    
██╔══██╗██║   ██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗    ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗    
██║  ██║╚██████╔╝╚██████╗██║  ██╗    ██║     ██║  ██║██║     ██║     ███████╗██║  ██║    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║    
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ")
# --------------------------------------------------------------------------------------------

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

# --------------------------------------------------------------------------------------------

if game == 0:
    if choice == 0:
        print(f"you choose {rock} and computer choose {rock} , got Tied")
    elif choice == 1:
        print(f"you choose {paper} and computer choose {rock} , You won !!")
    elif choice == 2:
        print(f"you choose {scissors} and computer choose {rock}, You lost  ")

# --------------------------------------------------------------------------------------------

if game == 1:
    if choice ==0:
        print(f"you choose {rock}, computer choose {paper}, you lost ")
    elif choice == 1:
        print(f"you choose {paper}, computer choose {paper} , both ties ")
    elif choice == 2:
        print(f"you choose {scissors}, computer choose {paper} , You won")

# --------------------------------------------------------------------------------------------

if game == 2:
    if choice == 0:
        print(f"you choose {rock}, computer choose {scissors}, you won ")
    elif choice == 1:
        print(f"you choose  {paper}, computer choose {scissors}, you lost")
    elif choice == 2:
        print(f"you choose {scissors} , computer choose {scissors}, both ties ")
