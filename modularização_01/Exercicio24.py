#Declaração de variaveis 
N1: int = 0
#Inicio

def main():
    global N1
    N1 = int(input("Digite o valor inteiro:"))
    divisivel_2_3()

def divisivel_2_3():
    global N1
    if N1 %2 ==0 and N1 %3 ==0:
        print("Divisivel por 2 e por 3")
    else:
        print("Não divisivel por 2 e por 3")

if __name__ == '__main__':
    main()

#Fim