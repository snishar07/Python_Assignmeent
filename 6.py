
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
            if i==1: instances[i] = Aircraft(2,4)
            if i==2: instances[i] = Aircraft(6,8)
            if i==3: instances[i] = Aircraft(10,12)
            if i==4: instances[i] = Aircraft(14,16)

    def final_x_y_coord(self):
        for i in range(len(instances)):
            print("\nAircraft [",i,"]")
            print("Final X-Coordinate:", instances[i].x)
            print("Final Y-Coordinate:", instances[i].y)

    def initial_x_y_coord(self):
        print("Creating New Aircraft Object:",i)
        print("New Aircraft Object has been Initalized:",i)
        print("Initial X-Coordinate:",instances[i].x)
        print("Initial Y-Coordinate:",instances[i].y)

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
        if i==0: instances[i] = Boeing_747(0,10,20,30)
        if i==1: instances[i] = Boeing_747(1,11,21,31)
        if i==2: instances[i] = Boeing_747(2,12,22,32)
        if i==3: instances[i] = Boeing_747(3,13,23,33)
        if i==4: instances[i] = Boeing_747(4,14,24,44)

        instances[i].initial_x_y_coord()
        print("New Boeing 747 Object Has Just Been Iniitalized:", i)
        print("X-Coordinate:",instances[i].x_d)
        print("Y-Coordinate:",instances[i].y_d)
        # instances[i].directions()
    instances[i].final_x_y_coord()

    def flight_path():
        for i in range(len(instances)):
            print("\nAircraft ",i)
            print("Starting from: (",instances[i].x,",",instances[i].y,")")
            print("Headed to: (",instances[i].x_d,",",instances[i].y_d,")")
            m=(instances[i].y_d-instances[i].y) / (instances[i].x_d-instances[i].x)
            b=instances[i].y-m*instances[i].x
            for j in range(instances[i].x, instances[i].x_d+1):
                y=m*j+b
                if(y<=instances[i].y_d):
                    print( j, ",", y)
            print("We have arrived")
            print("Acceleration Constant: 1")

    flight_path()
