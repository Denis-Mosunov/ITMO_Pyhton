import math

# Input
d1_yards = float(input("Enter shortest distance from rescuer to water's edge, d1 (yards) => "))
print(int(d1_yards))

d2_feet = float(input("Enter shortest distance from drowning person to shore, d2 (feet) => "))
print(int(d2_feet))

h_yards = float(input("Enter lateral displacement between rescuer and drowning person, h (yards) => "))
print(int(h_yards))

v_sand_mph = float(input("Enter rescuer's speed on sand, v_sand (mph) => "))
print(int(v_sand_mph))

n = float(input("Enter slowdown coefficient in water, n => "))
print(int(n))

theta1_degrees = float(input("Enter rescuer's direction angle, theta1 (degrees) => "))
print(int(theta1_degrees))

# Calculations
theta1_radians = math.radians(theta1_degrees)

d1_feet = d1_yards * 3
h_feet = h_yards * 3

x = d1_feet * math.tan(theta1_radians)

L1 = math.sqrt(x**2 + d1_feet**2)
L2 = math.sqrt((h_feet - x)**2 + d2_feet**2)

v_sand_fps = v_sand_mph * 5280 / 3600

t_seconds = (1 / v_sand_fps) * (L1 + n * L2)

# Output
print("If the rescuer starts moving at an angle theta1 =", int(theta1_degrees), "degrees, he")
print("will reach the drowning person in", round(t_seconds, 1), "seconds.")
