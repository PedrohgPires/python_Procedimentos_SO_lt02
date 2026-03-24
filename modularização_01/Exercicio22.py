#Declaração de variaveis 
N1: int = 0
N2: int = 0
#Inicio

def main():
    global N1,N2
    N1= int(input("Digite o primeiro valor:"))
    N2= int(input("Digite o segundo valor:"))
    maior()

def maior():
    global N1,N2
    if N1> N2 :
        print(N2,N1)
    elif N1==N2:
        print("São iguais", N1,N2)
    else:
        print(N1,N2)

if __name__ == '__main__':
    main()

#Fim