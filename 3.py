class Aircraft:

  def __init__(self):
    self.x = 0
    self.y = 0
    self.accleration = 1


  def move_left(self):
      self.x -= self.accleration


  def move_right(self):
      self.x += self.accleration


  def move_up(self):
      self.y += self.accleration


  def move_down(self):
      self.y -= self.accleration

print("Exercise 3 \n")

position = ["position1", "position2", "position3", "position4", "position5"]
for i in range(len(position)):

    position[i] = Aircraft()
    print("Creating a New Aircraft Object:",i)
    print("An Aircraft Object Has been Initalized:",i)
    print("Initial X-Coordinate-->",position[i].x)
    print("Initial Y-Coordinat-->",position[i].y)

for i in range(len(position)):
    if i==0:
        print("Aircraft position",i,"has moved up")
        position[i].move_up()
        print("Aircraft position",i,"has moved up")
        position[i].move_up()
        print("Aircraft position",i,"has moved up")
        position[i].move_up()
        print("Aircraft position",i,"has moved to the right")
        position[i].move_right()

    if i==1:
        print("Aircraft position",i,"has moved up")
        position[i].move_up()
        print("Aircraft position",i,"has moved to the left")
        position[i].move_left()
        print("Aircraft position",i,"has moved down")
        position[i].move_down()

    if i==2:
        print("Aircraft position",i,"has moved to the right")
        position[i].move_right()
        print("Aircraft position",i,"has moved down")
        position[i].move_down()
        print("Aircraft position",i,"has moved down")
        position[i].move_down()
        print("Aircraft position",i,"has moved to the left")
        position[i].move_left()
        print("Aircraft position",i,"has moved to the left")
        position[i].move_left()

    if i==3:
        print("Aircraft position",i,"has moved to the right")
        position[i].move_right()
        print("Aircraft position",i,"has moved down")
        position[i].move_down()
        print("Aircraft position",i,"has moved to the right")
        position[i].move_right()
        print("Aircraft position",i,"has moved down")
        position[i].move_down()
        print("Aircraft position",i,"has moved down")
        position[i].move_down()

    if i==4:
        print("Aircraft position",i,"has moved to the right")
        position[i].move_right()
        print("Aircraft position",i,"has moved down")
        position[i].move_down()
        print("Aircraft position",i,"has moved to the left")
        position[i].move_left()
        print("Aircraft position",i,"has moved Rto the right")
        position[i].move_right()
        print("Aircraft position",i,"has moved to the right")
        position[i].move_right()
        print("Aircraft position",i,"has moved to the right")
        position[i].move_right()
        print("Aircraft position",i,"has moved down")
        position[i].move_down()
        print("Aircraft position",i,"has moved up")
        position[i].move_up()
        print("Aircraft position",i,"has moved up")
        position[i].move_up()

for i in range(len(position)):
    print("\nAircraft [",i,"]")
    print("Final X-Coordinate-->", position[i].x)
    print("Final Y-Coordinat-->", position[i].y)
