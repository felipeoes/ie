import math

# UNIFORME

def calculatePdfUni(a: float, b: float, x: int):
    if x >= a and x <= b:
        return 1.0 / (b - a)
    return 0

def calculateCdfUni(a: float, b: float, x: int):
    if x >= a and x <= b:
        return (x - a )  / (b - a)
    return 0

def calculateHUni(a: float, b: float):
    return (a + b) / 2.0


def calculateVarUni(a: float, b: float):
    ba = b - a
    return math.pow(ba,2) / 12.0


# EXPONENCIAL

def calculatePdfExpo(lamb: float, x: int):
    if x >= 0:
        return lamb * math.exp( (-lamb * x) )
    return 0

def calculateCdfExpo(lamb: float, x: int):
    if x >= 0:
        return 1 - math.exp( (-lamb * x) )
    return 0

def calculateHExpo(lamb: float):
        return 1.0 / lamb
    
def calculateVarExpo(lamb: float):
    return 1.0 / math.pow(lamb)


# NORMAL

def calculatePdfNormal(mi: float, sigma: float, x: int):
    frac0 = 1 / math.sqrt( 2 * math.pi * sigma)
    frac1 = (-0.5) * math.pow( (x - mi) / sigma )
    frac2 = math.exp(frac1)
    
    return frac0 * frac2

def calculateVarNormal(sigma: float):
    return math.pow(sigma)


    


print("Calculadora de distribuições contínuas \n")
option = 0
stack = []
stackCdf = []

while option != 5:
    print("Selecione qual opção deseja: \n 1 - Distribuição Uniforme Contínua \n 2 - Distribuição Exponencial \n 3 - Distribuição Normal \n 4 - Somatória de todas as probabilidades \n 5 - Fechar o programa")
    option = int(input())

    if option == 1:
        print("Digite os parâmetros da função probabilidade da Distribuição Uniforme Contínua \nOBS: a, b, x. Ex: 0.7 3.5 2")
        INPUT = input().split(" ")
        a = float(INPUT[0])
        b = float(INPUT[1])
        x = int(INPUT[2])
        stack.append(calculatePdfUni(a, b, x))
        stackCdf.append(calculateCdfUni(a, b, x))
        print("PDF =", stack[-1])
        print("CDF =", stackCdf[-1])
        print("Esperança =", calculateHUni(a, b))
        print("Variância =", calculateVarUni(a, b))
    elif option == 2:
        print("Digite os parâmetros da função probabilidade da Distribuição Exponencial \nOBS: lambda, x. Ex: 2.0 3")
        INPUT = input().split(" ")
        lamb = float(INPUT[0])
        x = int(INPUT[1])
        stack.append(calculatePdfExpo(lamb, x))
        stackCdf.append(calculateCdfExpo(lamb, x))
        print("PDF =", stack[-1])
        print("CDF =", stackCdf[-1])
        print("Esperança =", calculateHExpo(lamb))
        print("Variância =", calculateVarExpo(lamb))
    elif option == 3:
        print("Digite os parâmetros da função probabilidade da Distribuição Normal \nOBS: mi: float, sigma: float, x: int. Ex: 0.383 2.3 3")
        INPUT = input().split(" ")
        mi = float(INPUT[0])
        sigma = int(INPUT[1])
        x = int(INPUT[2])
        stack.append(calculatePdfNormal(mi, sigma, x))
        print("PDF =", stack[-1])
        print("Esperança =", mi)
        print("Variância =", calculateVarNormal(sigma))
    elif option == 4:
        print("Somatória de todas as probabilidades: ")
        print("Somatória PDF = ", sum(stack))
        print("Somatória CDF = ", sum(stackCdf))
        stack.clear()
        stackCdf.clear()
    elif option == 5:
        print("Até mais!")
        break
    
    else:
        print("Opção inválida, escolha uma opção entre 1 e 5!")

    print("Seguir com a próxima operação? \n1 - Sim \n2 - Não")
    continueOption = int(input())
    if continueOption == 2:
        break
