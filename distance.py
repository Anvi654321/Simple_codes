import math
a=int(input("Enter the coordinates of the 1st x value"))
b= int(input("Enter the coordinates of the 1st y value"))
c= int(input("Enter the value of the 2nd x value"))
d= int(input("Enter the value of the 2nd y value"))
e= math.sqrt((c-a)**2+(d-b)**2)
print(e)