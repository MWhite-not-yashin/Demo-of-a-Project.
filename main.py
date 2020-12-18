import math
import secrets
s = secrets
print("Welcome to the Dungeon!")
name = input("Choose a Name: ")
perc = s.randbelow(100)
health = 100
print(name + " is in a small dungeon room")
if (perc == 100):
  print(name + " has perfect vision and sees a chest, a painting on the wall, and a small hole in the wall. Of course theres also the metal door.")
else:
  if (perc > 75):
    print(name + " has normal vision and sees a chest, and a painting on the wall, theres also something wrong with the wall near the Metal door.")
  else:
    if (perc > 50):
      print(name + " has poor vision, but can see a painting on the wall, a box, or a chest.")
    else:
      if (perc > 25):
        print(name + " has terrible vision, and can only see 2 blobs, one is on the wall and the other is on the ground.")
      else:
        if(perc > 0):
          print(name + " has atrocious vision and can only see a blob on the wall.")
        else:
          if(perc == 0):
            print(name + " is blind and trips on something on the floor, which slams his head against the metal door.")
            health = health - 100
if (health == 0):
  print(name + " has died in the dungeon!")
else:
  location = input("Which one does " + name + " go to? (Specific name it is Cap Sensitive!)")
  if (location == "Chest"):
    openc = input("There is a chest, its unlocked. Do you open it?")
    if (openc == "Yes"):
      print(name + " opens the chest, only to find its trapped!")
      print(name + " has died in the dungeon!")
    else:
      if (openc == "No"):
        print(name + " deiceds to not risk it. But when hes walking back a skeleton rises from a stone behind " + name + " and kills them!")
        print(name + " has died in the dungeon!")
      else:
        print(name + "'s attempt to function properly fails, and they die due to inability to say yes or no.")
        print(name + " has died in the dungeon!")
  else:
    if (location == "Painting"):
      print(name + " walks up to the painting, where it has small holes in it, upon closer inspection, these are dart holes! You try to get away but they fire and you die of poisonous darts!")
      print(name + " has died in the dungeon!")
    else:
      if (location == "Hole"):
        print("There is a small hole in the wall. " + name + " thinks they can see a key in there! " + name + " grabs it and unlocks the metal door.")
        print(name + " has escaped the dungeon!")
      else:
        if (location == "Door"):
          print(name + " walks up to the door to see its locked, upon trying to walk away they step on a pressure plate and get pelted with arrows!")
          print(name + " has died in the dungeon!")
        else:
          print("Due to either your lack of sight, refusal to go anywhere, or spelling mistakes, you did not go anywhere. A timer goes off which then fills the room with water.")
          print(name + " has died in the dungeon!")