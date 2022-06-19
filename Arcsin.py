import math

e, x = map(float, input().split())

a2 = math.pi / 2
a1 = - math.pi / 2

while True:
    if (a2 - a1) < e:
        break
    
    vasat_baze = (a1 + a2) / 2

    if math.sin(vasat_baze) > x :
        a2 = vasat_baze

    if math.sin(vasat_baze) <= x :
        a1 = vasat_baze

print(round(vasat_baze, 4))
