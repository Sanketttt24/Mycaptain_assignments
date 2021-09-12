#code1
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius "  , r  ," is: " ,  pi * r**2)


#code2
filename = input("input the file name:")
f_extns = filename.split(".")
print("the extension of file is:",f_extns[-1])