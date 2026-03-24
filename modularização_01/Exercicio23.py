#Declaração de variaveis 
N1: float = 0
N2: float = 0
N3: float = 0
N4: float = 0
#Inicio

def main():
    global N1,N2,N3,N4
    N1= float(input("Digite o primeiro valor:"))
    N2= float(input("Digite o segundo valor:"))
    N3= float(input("Digite o terceiro valor:"))
    N4= float(input("Digite o quarto valor:"))
    crescente()

def crescente():
    global N1,N2,N3,N4
    if N3>=N2 and N2>=N1:   
        if N4<=N1:
            print(N4,N1,N2,N3)
        elif N4<=N2:
            print(N1,N4,N2,N3)
        elif N4<=N3:
            print(N1,N2,N4,N3)
        else:
            print(N1,N2,N3,N4)
    else:
        print("Digite os tres primeiros em ordem crescente (quarto valor não necessariamente em ordem)")

if __name__ == '__main__':
    main()

#Fim