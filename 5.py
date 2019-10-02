class Aircraft:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(self.x)
        print(self.y)

    def move_left(self):
        self.x = self.x-1

    def move_right(self):
        self.x = self.x+1

    def move_up(self):
        self.y = self.y+1

    def move_down(self):
        self.y = self.y-1

    instances=["instance1", "instance2", "instance3", "instance4", "instance5"]
    def instance_create(self):
        for i in range(len(instances)):
            if i==0: instances[i] = Aircraft(0,2)
            if i==1: instances[i] = Aircraft(4,6)
            if i==2: instances[i] = Aircraft(8,10)
            if i==3: instances[i] = Aircraft(12,14)
            if i==4: instances[i] = Aircraft(16,18)

    def final_x_y_coord(self):
        for i in range(len(instances)):
            print("\nAircraft [",i,"]")
            print("Final X-Coord:", instances[i].x)
            print("Final Y-Coord:", instances[i].y)

    def initial_x_y_coord(self):
        print("Creating New Aircraft Object:",i)
        print("New Aircraft Object has been Initalized:",i)
        print("Initial X-Coord:",instances[i].x)
        print("Initial Y-Coord:",instances[i].y)

    def directions(self):
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

class Boeing_747(Aircraft):

    def __init__(self,x,y,x_d,y_d):
        self.x = x
        self.y = y
        self.x_d = x_d
        self.y_d = y_d


if __name__=='__main__':

    instances=["instance1", "instance2", "instance3", "instance4", "instance5"]
    for i in range(len(instances)):
        if i==0: instances[i] = Boeing_747(10,20,30,40)
        if i==1: instances[i] = Boeing_747(11,21,31,41)
        if i==2: instances[i] = Boeing_747(12,22,32,42)
        if i==3: instances[i] = Boeing_747(13,23,33,43)
        if i==4: instances[i] = Boeing_747(14,24,34,44)

        instances[i].initial_x_y_coord()
        print("New Boeing 747 Object ahs been Iniitalized:", i)
        print("X-Coord:",instances[i].x_d)
        print("Y-Coord:",instances[i].y_d)
        instances[i].directions()
    instances[i].final_x_y_coord()

