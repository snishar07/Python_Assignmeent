
# A Basic Aircraft

# Exercise 1-part 1
print("Exercise 1-part 1")
aircrafts = {"x": 10, "y": 20}

print(aircrafts["x"])
print(aircrafts["y"])


# Exercise 1-part 2
print("\nExercise 1-part 2")
Aircrafts = ["aircraft-1", "aircraft-2", "aircraft-3", "aircraft-4", "aircraft-5"]
coordinates = [30,40, 50,60, 70,80, 90,100, 110,120]

var = 0
for aircraft in Aircrafts:
    print(aircraft, "The coordinates are: ", coordinates[var], coordinates[var+1])
    var+= 2

