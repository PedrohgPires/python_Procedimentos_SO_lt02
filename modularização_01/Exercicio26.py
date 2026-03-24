#Declaração de variaveis 
n1: int = 0
n2: int = 0
#Inicio

def main():
    global n1,n2
    n1 = int(input("Digite o primeiro valor inteiro:"))
    n2= int(input("Digite o segundo valor inteiro:"))
    verificacao_multiplo()

def verificacao_multiplo():
    global n1,n2
    if n1 == 0 or n2 == 0:
        print("Não é possível verificar múltiplo com zero")
    elif n1 >=n2:
        if n1% n2 ==0:
            print(n1,"é multiplo de ",n2) 
        else:
             print(n1,"não é multiplo de ",n2) 
    else:
        if n2% n1 ==0:
            print(n2,"é multiplo de ",n1) 
        else:
            print(n2,"não é multiplo de ",n1) 


if __name__ == '__main__':
    main()

#Fim