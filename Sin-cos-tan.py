import math

angle = math.radians(float(input("Type an angle: ")))
while angle < 0 and angle > 360:
    print("The angle must be between 0 and 360")
    angle = math.radians(float(input("Try again: ")))

print (f"Sine:  {round(math.sin(angle),4)}")
print (f"Cosine:  {round(math.cos(angle),4)}")
print (f"Tangent: {round(math.tan(angle),4)}")