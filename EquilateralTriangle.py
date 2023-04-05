import matplotlib.pyplot as plt
import random
import math 

#Lenght of the triangle
L = random.randint(1,50)

#Coordinates of the triangle
x = random.randint(1,10)
y = random.randint(1,10)
vertex = (x, y)

# Calculate the coordinates of the other two vertices
x1 = x + L * math.cos(60)
y1 = y + L * math.sin(60)
vertex1 = (x1, y1)

x2 = x + L * math.cos(-60)
y2 = y + L * math.sin(-60)
vertex2 = (x2, y2)

#Grouping the coordinates
x_coordinates = [x, x1, x2]
y_coordinates = [y, y1, y2]

#Plotting the dots
plt.scatter(x_coordinates, y_coordinates, color= "black", 
            marker= ".", s=30)


# Set the size of the plot by inches
plt.gcf().set_size_inches(6, 6)

# Plot the equilateral triangle
plt.plot([x, x1], [y, y1], color='black')
plt.plot([x1, x2], [y1, y2], color='black')
plt.plot([x2, x], [y2, y], color='black')
plt.title("Plot with sizing by inches")

#Show the plot
for i_x, i_y in zip(x_coordinates, y_coordinates):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y), size = 7)
plt.show()

#Show another plot with equal sizing for the axes
plt.scatter(x_coordinates, y_coordinates, color= "black", marker= ".", s=30)
plt.xlim(-50,50)
plt.ylim(-50,50)
plt.plot([x, x1], [y, y1], color='black')
plt.plot([x1, x2], [y1, y2], color='black')
plt.plot([x2, x], [y2, y], color='black')
plt.title("Plot with limit sizing")
for i_x, i_y in zip(x_coordinates, y_coordinates):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y), size = 5)
plt.show()

#Checking the distance between each pair of coordinates
print(f'Distance between {vertex} and {vertex1}: {math.dist([x],[x1])} ')
print(f'Distance between {vertex1} and {vertex2}: {math.dist([x],[x2])}')
print(f'Distance between {vertex2} and {vertex}: {math.dist([x2],[x])}')
