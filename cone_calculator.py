"""
Cone Surface Area and Volume Calculator
Author: Parad0x
v1.2
01/25/22
Displays the volume and surface area of a cone with supplied radius and height.
"""

import math

def GetAndCheckNum(variableName):
    outVariable = None
    while outVariable == None:
        inVariable = input(f"Enter your cone's {variableName} in inches: ")
        try:
            outVariable = (float)(inVariable)
            return outVariable
        except:
            print (f"You entered an invalid {variableName}. Please try numbers.")

def GetSurfaceArea(radius, height):
    surfaceArea = math.pi * radius * (radius+math.sqrt(pow(height,2)+pow(radius,2)))
    round(surfaceArea,3)
    return surfaceArea

def GetVolume(radius, height):
    volume = (1/3) * math.pi * pow(radius, 2) * height
    round(volume,3)
    return volume

radius = GetAndCheckNum("radius")
height = GetAndCheckNum("height")

print (f"""
Cone surface area is: {GetSurfaceArea(radius, height)} in^2
Cone volume is: {GetVolume(radius, height)} in^2
""")


