
class Aircraft:

  def __init__(self):
    self.x = 0
    self.y = 0
    self.accleration = 1


  def move_left(self):
      print ("Moved to the left")
      self.x -= self.accleration


  def move_right(self):
      print ("Moved to the right")
      self.x += self.accleration


  def move_up(self):
      print ("Moved up")
      self.y += self.accleration


  def move_down(self):
      print ("Moved down")
      self.y -= self.accleration

  def show_pos(self):
    print (self.x," ", self.y)

print("Exercise 2")
position = Aircraft()
print("Initial X-Coordinate:", position.x)
print("Initial Y-Coordinate:", position.y)

position.move_right()
position.move_right()
position.move_up()
position.move_down()
position.move_down()
position.move_right()
position.move_right()
position.move_left()
position.move_up()
position.move_up()
position.move_down()
position.move_up()
position.move_down()
position.move_up()
print("Final X-Coordinate:", position.x)
print("Final Y-Coordinate:", position.y)
