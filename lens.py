import math

def FOVfromAngleD(_angFOV, _WD):
    hang = float(_angFOV)/2
    fWD = float(_WD)
    hFOV = abs(math.tan(hang)*fWD)
    FOV = 2*hFOV
    return FOV
print("This is basic lens calculator")

angFOV = input("Write angular field of view [degrees]: ")
WD = input("Write working distance [mm]: ")

print("Field of view of your camera setup is " + str(FOVfromAngleD(angFOV,WD)) + "mm")


