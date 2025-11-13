area=lambda a:a*a
side=int(input("enter the side of square:"))
print("area of the square is",area(side))
rarea=lambda l,b:l*b
l=int(input("enter the length of the rectangle"))
b=int(input("enter the breadth of the rectangle"))
print("area of the rectangle:",rarea(l,b))
tarea=lambda c,h:0.5*c*h
c=int(input("enter the breadth of the traingle:"))
h=int(input("enter the height of the traingle:"))
print("area of traingle is:",tarea(c,h))
