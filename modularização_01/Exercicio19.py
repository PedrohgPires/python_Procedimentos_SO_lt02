#Declaração de variaveis 
N1: float = 0
N2: float = 0
resultado: float = 0
#Inicio

def main():
    global N1, N2, resultado
    N1 = float(input("Digite o primeiro numero:"))
    N2 = float(input("Digite o segundo numero:"))
    maior()
    
def maior():
    global N1,N2,resultado
    if N1 > N2:
        print(N1,"É maior que",N2)
    elif N1 == N2:
        print("São numeros iguais",N2)
    else:
        print(N2,"É maior que",N1)

if __name__ == '__main__':
    main()

#Fim