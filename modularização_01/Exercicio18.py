#Declaração de variaveis 
N1: int = 0
N2: int = 0
resultado: int = 0
#Inicio
def main():
    global N1, N2, resultado
    N1 = int(input("Digite o primeiro numero:"))
    N2 = int(input("Digite o segundo numero:"))
    diferenca()

def diferenca():
    global N1, N2, resultado
    if N1 > N2:
        resultado = N1-N2
    else:
        resultado = N2-N1
    print(resultado)    



if __name__ == '__main__':
    main()
#Fim