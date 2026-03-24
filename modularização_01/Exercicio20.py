#Declaração de variaveis 
a: float = 0
b: float = 0
c: float = 0
delta: float = 0
x1: float = 0
x2: float = 0
#Inicio

def main():
    global a, b, c, x1,x2, delta
    a = float(input("Digite o coeficiente a:"))
    b = float(input("Digite o coeficiente b:"))
    c = float(input("Digite o coeficiente c:"))
    calcula_delta()

def calcula_delta():
    global a,b,c,delta
    delta = (b*b)-4*a*c
    raiz()

def raiz():
    import math
    global a, b, delta, x1, x2
    if(a==0):
        print("Não é uma equação do segundo grau")
    elif delta >0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Duas raizes",x1,x2)
    elif delta < 0:
        print("Não possui raizes")
    else:
        x1 = -b/(2*a)
        print("Possui uma raiz",x1)

if __name__ == '__main__':
    main()

#Fim