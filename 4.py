class Aircraft:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_left(self):
        self.x = self.x-1

    def move_right(self):
        self.x = self.x+1

    def move_up(self):
        self.y = self.y+1

    def move_down(self):
        self.y = self.y-1


if __name__=='__main__':

    instances=["instance1", "instance2", "instance3", "instance4", "instance5"]

    def directions():
        instances[i].move_right()
        instances[i].move_right()
        instances[i].move_up()
        instances[i].move_right()
        instances[i].move_left()
        instances[i].move_up()
        instances[i].move_up()
        instances[i].move_down()
        instances[i].move_up()
        instances[i].move_down()
        instances[i].move_up()
    def final_x_y_coordinate():
        for i in range(len(instances)):
            print("\nAircraft [",i,"]")
            print("Final X-Coordinate:", instances[i].x)
            print("Final Y-Coordinate:", instances[i].y)

    for i in range(len(instances)):
        if i==0: instances[i] = Aircraft(0,0)
        if i==1: instances[i] = Aircraft(2,4)
        if i==2: instances[i] = Aircraft(6,8)
        if i==3: instances[i] = Aircraft(10,12)
        if i==4: instances[i] = Aircraft(12,14)

        print("Creating New Aircraft Object:",i)
        print("New Aircraft Object has been Initalized:",i)
        print("Initial X-Coordinate:",instances[i].x)
        print("Initial Y-Coordinate:",instances[i].y)
        directions()

    final_x_y_coordinate()
