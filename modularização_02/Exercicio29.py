#Declaração de variaveis 
valor: float = 0
tipo: int = 0
#Inicio

def main():
    tipo = int(input("Digite o tipo de investimento (1 = poupança e 2 = renda fixa):"))
    valor = float(input("Digite o valor do investimento:"))
    verificacao_investimento(tipo,valor)

def  verificacao_investimento(investimento,quantia):
    corrigido: float = 0
    if investimento ==2:
        corrigido = quantia+(quantia*0.05)
        print("Valor corrigido:", corrigido)
    elif investimento ==1:
        corrigido = quantia+(quantia*0.03)
        print("Valor corrigido:", corrigido)
    else:
        print("Digite 1 ou 2 (1 = poupança e 2 = renda fixa)") 


if __name__ == '__main__':
    main()

#Fim