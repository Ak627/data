import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Tuples, lists, and dictionaries")
screen.fill((0,0,0))

#tuples()
Friends = ("Sebastian", "Jacob", "Kevin", "Damacio", "Ale")

GREEN = (76, 217, 106)


for i in range(len(Friends)):
    print(Friends[i], end = " ")
print()

print(Friends[2])

#list[]
CircleList = [(100,100), (200, 300), (400, 100), (100, 450), (400,400)]



screen.fill((0,0,0))

for i in range(len(CircleList)):
    pygame.draw.circle(screen, GREEN, (CircleList[i]), 50)
pygame.display.flip()

#dictionaries{}
favMenu = {"SnarfBurger" : 5.95,
                 "ChickenSandwich" : 8.20,
                 "FrenchFries" : 3.05,
                 "GrilledCheese" : 3.25,
                 "Soda" : 2.75}



while True:
    print("SnarfBurger Menu items", favMenu)
    print("What would you like to order?")
    item = input()
    if item == "SnarfBurger":
        print("That is $", favMenu["SnarfBurger"])
    elif item == "ChickenSandwich":
        print("That is $", favMenu["ChickenSandwich"])
    elif item == "FrenchFries":
        print("That is $", favMenu["FrenchFries"])
    elif item == "GrilledCheese":
        print("That is $", favMenu["GrilledCheese"])
    elif item == "Soda":
        print("That is $", favMenu["Soda"])
    elif item == 'q':
        break
    else:
        print("That item is not on the menu")
pygame.quit()
