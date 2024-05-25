##Follow instructins from College Board and create your most simple performance task that meets all requirements.  Note: This is not a project you can submit to the College Board....why?  teacher is reviewing it!

#pokemon compatibility test
import random
import numpy as np
from collections import Counter

fire = ["Charmander", "Cyndaquil", "Torchic", "Chimchar","Litten", "Fennekin", "Litwick", "Scorbunny", "Fuecoco"]

water = ["Squirtle", "Totodile", "Mudkip", "Piplup", "Oshawott", "Froakie", "Popplio", "Sobble", "Quaxly"]

grass = ["Bulbasaur", "Treecko", "Turtwig", "Chikorita", "Snivy", "Chespin", "Rowlet", "Grookey", "Sprigatito"]


electric = ["Pikachu", "Eevee", "Voltorb", "Electrode", "Pichu", "Mareep", "Electrike", "Raichu", "Pikipek"]


answers = []


def spareTime(answers):
  print("What do you do with your spare time?\n")
  print("A. Swimming")
  print("B. Reading")
  print("C. Playing video games")
  print("D. Playing sports")
  choice = input("\nEnter your choice: ")
  if choice =="A":
    answers.append("water")
  elif choice =="B":
    answers.append("fire")
  elif choice =="C":
    answers.append("electric")
  elif choice =="D":
    answers.append("grass")
  else:
    print("That is not a valid answer")
    spareTime(answers)
    

def element(answers):
  print("What element do you relate the most?\n")
  print("A. Fire")
  print("B. Water")
  print("C. Grass")
  print("D. Electric")
  choice = input("\nEnter your choice: ")
  if choice =="A":
    answers.append("fire")
  elif choice =="B":  
    answers.append("water")
  elif choice =="C":
    answers.append("grass")
  elif choice =="D":
    answers.append("electric")
  else:
    print("That is not a valid answer")
    element(answers)  
  


def superpower(answers):
  print("If you had a superpower, what would it be?\n")
  print("A. To spitfire")
  print("B. Super strength")
  print("C. To be able to breathe underwater")
  print("D. Telekinesis")
  choice = input("\nEnter your choice: ")
  if choice =="A":
    answers.append("fire")
  elif choice =="B":
    answers.append("grass")
  elif choice =="C":
    answers.append("water")
  elif choice =="D":
    answers.append("electric")
  else:
    print("That is not a valid answer")
    superpower(answers)

def apocalypse(answers):
  print("What would you do in a zombie apocalypse?\n")
  print("A. Fight the zombies")
  print("B. Run away")
  print("C. Hide")
  print("D. Become a zombie")
  choice = input("\nEnter your choice: ")  
  if choice =="A":
    answers.append("fire")
  elif choice =="B":
    answers.append("water")
  elif choice =="C":
    answers.append("grass")
  elif choice =="D":
    answers.append("electric")
  else:
    print("That is not a valid answer")
    apocalypse(answers)

def fightingStyle(answers):
  print("What is your fighting style?\n")
  print("A. Close combat")
  print("B. Ranged combat")
  print("C. Strong defense")
  print("D. Strong offense")
  choice = input("\nEnter your choice: ")
  if choice =="A":
    answers.append("fire")
  elif choice =="B":
    answers.append("water")
  elif choice =="C":
    answers.append("grass")
  elif choice =="D":
    answers.append("electric")
  else:
    print("That is not a valid answer")
    fightingStyle(answers)
  
def Pokemon(answers):
  a = answers
  c = Counter(a)

  if c.most_common(1)[0][0] == "fire":
      pokemon = [fire[random.randint(0, len(fire) - 1)] for _ in range(3)] 
      print("Congrats, youngling! You are compatible with:\n")
      for i in pokemon:
        print(i)

  elif c.most_common(1)[  0][0] == "water":
      pokemon = [water[random.randint(0, len(water) - 1)] for _ in range(3)] 
      print("Congrats, youngling! You are compatible with:\n")
      for i in pokemon:
        print(i)

  elif c.most_common(1)[0][0] == "grass":
      pokemon = [grass[random.randint(0, len(grass) - 1)] for _ in range(3)] 
      print("Congrats, youngling! You are compatible with:\n")
      for i in pokemon:
        print(i)

  elif c.most_common(1)[0][0] == "electric":
      pokemon = [electric[random.randint(0, len(electric) - 1)] for _ in range(3)] 
      print("Congrats, youngling! You are compatible with:\n")
      for i in pokemon:
          print(i)

      

while True:
  print("Hello traveler! Welcome to the world of Pokemon! We will find the pokemon that best fits your personality. Wanna meet your poke friend? This is you place!!!")
  start = input("Type Start to begin!: ")
  if start == "Start":
        print("Great! Let's get started!")
        name = input("First, let's get to know each other. What's your name?: ")

        print(f"Alright {name}. Let's start the test!")
        spareTime(answers)
        element(answers)
        superpower(answers)
        apocalypse(answers)
        fightingStyle(answers)

        Pokemon(answers)
        break
  else:
        print("Error.Please type 'Start' to begin!")
        continue

  