print( """_                                     _     _                 _ 
     | |                                   (_)   | |               | |
     | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
     | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
     | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
      \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

""")
print("welcome to treaure island. Your mission is to find the treasure")
choice1 = input('you\'re at a crossroad, where do you want to go? Type "left" or right\n').lower()
if choice1=="left":
  choice2=input('you\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
  if choice2=="wait":
      choice3=input("you arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
      if choice3=="red":
        print("It's a room full of fire. Game Over.")
      elif choice3=="yellow":
        print("You found the treasure! You Win!")
      elif choice3=="blue":
        print("You enter a room of beasts. Game Over.")
      else:
        print("You chose a door that doesn't exist. Game Over.")
  else:
      print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
