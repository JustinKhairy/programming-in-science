# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t): #this is my solution to the first problem
    result=h0-(1/2*9.8*t**2) #formula
    return result
h0=float(input("What height was the ball dropped from (in meters):"))#variable for height dropped
t=float(input("how long has the ball been falling for (in seconds):"))#variable for time 

print("the ball is", str(calculate_height(h0, t)), "meters from the ground")


# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(time):
    Distance = 20*time
    return Distance

time=float(input("Enter time for car(in seconds):"))
print("The car will travel", str(calculate_car_distance(time)), "meters in", time, "seconds")
