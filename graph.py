import matplotlib.pyplot as plt
import math
from random import *
numerous=int(input("How Many Graphs"))
reference=[]
for looping in range(0,numerous):
    #Storing Coordinates
    numx = []
    numy = []
    #Time start from zero
    t = 0
    #Indicator to skip the first coordinate (checking the coordinate values)
    xtravel = 0
    #Degree and Velocity Input
    while True:
        try:
            degrees=int(input("Insert Degrees"))
            speeds=int(input("Insert Velocity"))
            break
        except:
            print("Invalid")
            continue
    while True:
        sog = math.radians(degrees)
        sig = math.sin(sog)
        cog = math.cos(sog)
        speed = speeds
        ray = (speed * sig * t) - ((10 * (t ** 2)) / 2)
        rax = speed * cog * t
        numx.append(rax)
        numy.append(ray)
        t += 0.001
        xtravel += 1
        if xtravel > 1:
            if ray < 0:
                break
            else:
                continue
    plt.scatter(numx, numy, c=choice(['red','green','blue','yellow','orange','black','lime','navy','gold']), edgecolor='none', s=randrange(10,51))
    items=max(numy)
    reference.append(items)
plt.legend(reference)
plt.xlabel("X-Coordinate")
plt.ylabel("Y-Coordinate")
plt.title("Projectile Motion of Balls")
plt.show()