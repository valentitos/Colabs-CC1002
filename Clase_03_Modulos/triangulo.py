#perimetro: num num num -> num
#calcula el perimetro de un triangulo de lados a b y c #ejemplo: perimetro(3,4,5) entrega 12
def perimetro(a,b,c):
    return a + b +c 

#Test
assert perimetro(3,4,5) == 12


#area: num num num -> float
#calcula el area de un triangulo de lados a b y c
#ejemplo: area(3,4,5) entrega 6
def area(a,b,c):
    semi = perimetro(a,b,c)/2
    return (semi*(semi-a)*(semi-b)*(semi-c))**0.5

#Test
assert area(3,4,5) == 6.0
