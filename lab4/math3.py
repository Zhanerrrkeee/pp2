from math import tan,pi,floor
num_of_sides=int(input())
length=int(input())
area=floor((num_of_sides*length**2)/(4*tan(pi/num_of_sides)))
print('The area of the polygon is:', area)
