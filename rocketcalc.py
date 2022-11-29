"""
Rocket Launch Calculator
v1
Author: Parad0x

Calculates the final height and velocity of a rocket with pre-set parameters. All units are SI units.
"""

Mfuel = 182000
MPayload = 4600

steps = 10000000
GRAVITY = 9.8
MrFuel = 200000
MEngine = 4000
ENGINE_FORCE = 3000000
tBurn = 240*(Mfuel/MrFuel)
dt = tBurn/steps
dm = Mfuel/steps
MRocket = Mfuel+MPayload+MEngine

curStep,Vi,Vf,H,dH,a = 0,0,0,0,0,0

def HuntValues (HeightFind: int, VelocityFind: int) -> tuple: 
    """
    ###CURRENTLY DISABLED###
    
    Attempts to modify the input values for a more ideal value
    """
    HeightGotten = 0
    VelocityGotten = 0
    while ():
        HeightGotten = 0
    return (HeightGotten, VelocityGotten)

values = HuntValues(400000, 7500)
TargetHeight = values[0]
TargetVelocity = values[1]

while (curStep <= steps):
    curStep += 1
    a = (ENGINE_FORCE/MRocket-GRAVITY)
    MRocket -= dm
    Vi = Vf
    if curStep > steps:
        Vf = Vi
    else:
        Vf = Vi + a*dt
    H = H + dH
    dH = .5*(Vi+Vf)*dt    

print(f"Final Velocity: {Vf}\nFinal Height: {H}")
