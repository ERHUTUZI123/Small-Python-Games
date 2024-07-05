import random

def play():
    x = input("please enter r(rock), s(scissors) or p(paper): ").lower()
    comp = random.choice(["r", "s", "p"])
    while x == comp:
        print("It's a Tie.")
        break

    while x != comp:
        win(x, comp)
        break

def win(player, opponent):
         if player == "r" and opponent == "s":
             print("You win!")  
             
         
         elif player == "s" and opponent == "p":
            print("You win!")  
            

         elif player == "p"and opponent == "r":
             print("You win!")
        
         else:
              print("You lose!")
        
         
play()
