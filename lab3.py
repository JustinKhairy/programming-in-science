import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta):
    x=r*math.cos(math.radians(theta))
    y=r*math.sin(math.radians(theta))
    return (round(x,5), round(y,5))
r=float(input("what is your radius"))
theta=float(input("What angle"))
print(f"your coordinates are: {str(polar_to_cartesian(r, theta))}")

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    r=math.sqrt((x**2)+(y**2))
    theta=math.degrees(math.atan((y/x)))
    return (round(r,5), round(theta,5))
x=float(input("Whats your x coordinate:"))
y=float(input("Whats your y coordinate:"))
print(f"your polar coordinates are: {cartesian_to_polar(x, y)} ")

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    w=2*math.pi*f
    x=A*(math.cos(w*t+math.radians(phi)))
    return (x)
A=float(input("What is the amplitude:"))
f=float(input("what is the frequency:"))
phi=float(input("what is the phase constant:"))
t=float(input("how much time has passed:"))

print(f"the position of the pendulum is: {round(pendulum_position(A, f, phi, t),5)}")