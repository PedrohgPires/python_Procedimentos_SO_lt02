#Declaração de variaveis 
hi: int = 0
hf: int = 0
mi: int = 0
mf: int = 0
mit: int = 0
mft: int = 0
respostaH: int = 0
respostaF: int = 0
#Inicio

def main():
    global hi, hf, mi, mf, mit, mft, respostaH, respostaF
    hi= int(input("Digite  hora inicial: "))
    mi = int(input("Digite o minuto inicial: "))
    hf= int(input("Digite a hora final: "))
    mf = int(input("Digite o minuto final: "))
    convrt_Min()
    verificacao()

def convrt_Min():
    global hi, hf, mi, mf, mit, mft, respostaH, respostaF
    mit = (hi*60)+mi
    mft = (hf*60)+mf
    respostaH = (mft-mit)//60
    respostaF = (mft-mit)%60

def verificacao():
    global respostaH, respostaF, mft, mit
    if(mft < mit):
        respostaH = ((1440-mit)+mft)//60
        respostaF = ((1440-mit)+mft)%60
    print(respostaH," horas e ", respostaF," minutos")
if __name__ == '__main__':
    main()

#Fim