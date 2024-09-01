import math
x1 = float(input("Input the x1 coordinate: "))
y1 = float(input("Input the y1 coordinate: "))

x2 = float(input("Input the x2 coordinate: "))
y2 = float(input("Input the y2 coordinate: "))

# slope

slope = abs(y1-y2) / abs(x1-x2)

print("The slope is:",slope)

## mid point coordinates

x_midpoint_coordinates = (x1 + x2)/2
y_midpoint_coordinates = (y1+y2)/2
print("The mid point coordinates is:", x_midpoint_coordinates,",", y_midpoint_coordinates,"\n")

### perpendicular bisector slope

bisector_perpendicular_slope = -1/slope

#### y intercept

y_intercept = y_midpoint_coordinates - slope * x_midpoint_coordinates

#### Perpendicular bisector function

y_intercept_perpendicular_bisector = -bisector_perpendicular_slope*x_midpoint_coordinates+y_midpoint_coordinates


print("The bisector segment coordinates => ({}, {}) and ({}, {})".format(x1, y1, x2, y2))
print("The perpendicular bisector equation => y = {}x + {}".format(bisector_perpendicular_slope, (-bisector_perpendicular_slope*x_midpoint_coordinates+y_midpoint_coordinates)))