#Declaração de variaveis 
preco: int = 0
vendas: int = 0
#Inicio

def main():
    preco = int(input("Digite o preço do produto:"))
    vendas= int(input("Digite a media mensal de vendas desse produto:"))
    verificacao(preco,vendas)

def verificacao(valor,quantVendas):
    if quantVendas<500 and valor<30:
        valor = (valor*0.1)+valor 
        print("Novo preço é: ",valor)
    elif quantVendas >= 500 and quantVendas < 1000 and valor >= 30 and valor < 80:
        valor = (valor*0.15)+valor
        print("Novo preço é: ",valor)
    elif quantVendas>=1000 and valor>=80:
        valor = valor-(valor*0.05)
        print("Novo preço é: ",valor)
    else:
        print("Preço igual: ",valor) 


if __name__ == '__main__':
    main()

#Fim