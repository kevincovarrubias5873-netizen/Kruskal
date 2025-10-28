import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    y = (x_2 - x_1)
    r = y ** 2
    o = (y_2 - y_1)
    n = o ** 2
    z = r + n
    res = math.sqrt(z)
    return res
