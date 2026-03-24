#Declaração de variaveis 
N1: float = 0
N2: float = 0
N3: float = 0
N4: float = 0
media: float = 0
#Inicio

def main():
    global N1,N2,N3,N4,media
    N1= float(input("Digite a primeira nota:"))
    N2= float(input("Digite a segunda nota:"))
    N3= float(input("Digite a terceira nota:"))
    N4= float(input("Digite a quarta nota:"))
    calcula_media()

def calcula_media():
    global N1,N2,N3,N4,media
    media = (N1+N2+N3+N4)/4
    print("Media:",media)
    if media >=6:
        print("Aprovado")
    elif media>=3:
        print("Exame")
    else:
         print("Retido")



if __name__ == '__main__':
    main()

#Fim