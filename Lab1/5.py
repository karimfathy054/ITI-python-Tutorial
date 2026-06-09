# I know we did not mention try and except in the session but I use python for more than 5 years now 
# I find the try except block is easier than checking if the input is digits or not before cast to a float 
try:
    base = float(input("enter the base: "))
    height = float(input("enter the height: "))
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    area = 1/2 * base * height
    print("area: ",area)
except ValueError as e:
    print("Error: ",e)