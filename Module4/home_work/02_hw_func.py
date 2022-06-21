# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    l = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return l


xa = 1 # AB 3.1622776601683795
ya = 3
xb = 4 # BC 2.23606797749979
yb = 4
xc = 3  # AC 2.23606797749979   
yc = 2

if distance(xa, ya, xb, yb) < distance(xb, yb, xc, yc) and distance(xa, ya, xb, yb) < distance(xa, ya, xc, yc):
    print("Самый короткий АВ")
elif distance(xb, yb, xc, yc) < distance(xa, ya, xc, yc):
    print("Самый короткий BC")
else:
    print("Самый короткий AC")
