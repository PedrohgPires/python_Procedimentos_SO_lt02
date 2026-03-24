#Declaração de variaveis 
n1: int = 0
n2: int = 0
#Inicio

def main():
    n1 = int(input("Digite o primeiro valor inteiro:"))
    n2= int(input("Digite o segundo valor inteiro:"))
    verificacao_multiplo(n1,n2)

def verificacao_multiplo(nota1,nota2):
    if nota1 == 0 or nota2 == 0:
        print("Não é possível verificar múltiplo com zero")
    elif nota1 >=nota2:
        if nota1% nota2 ==0:
            print(nota1,"é multiplo de ",nota2) 
        else:
             print(nota1,"não é multiplo de ",nota2) 
    else:
        if nota2% nota1 ==0:
            print(nota2,"é multiplo de ",nota1) 
        else:
            print(nota2,"não é multiplo de ",nota1) 


if __name__ == '__main__':
    main()

#Fim