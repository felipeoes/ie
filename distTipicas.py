import math

# UNIFORME


def calculateProbUni(a: float, b: float, x: int):
    if x >= a and x <= b:
        return 1.0 / (b - a + 1)
    return 0


def calculateHUni(a: float, b: float):
    return (a + b) / 2.0


def calculateVarUni(a: float, b: float):
    ba = b - a
    return ba * (ba + 2) / 12.0

# BERNOULLI


def calculateProbBern(p: float, x: int):  # x assume 0 ou 1
    if x == 0 or x == 1:
        return math.pow(p, x) * math.pow(1 - p, 1 - x)
    return 0


def calculateVarBern(p: float):
    return p * (1 - p)

# BINOMIAL


def calculateProbBin(p: float, n: int, x: int):
    if x >= 0 and x <= n:
        combNX = math.factorial(
            n) / (math.factorial((n - x)) * math.factorial(x))

        return combNX * math.pow(p, x) * math.pow(1 - p, n - x)
    return 0


def calculateHBin(p: float, n: int):
    return p * n


def calculateVarBin(p: float, n: int):
    return n * p * (1 - p)

# HIPERGEOMÉTRICA


def calculateProbHyper(A: int, B: int, n: int, x: int):
    if(max(0, (n - B)) <= x and min(n, A) >= x):
        AB = A + B
        combA = math.factorial(
            A) / (math.factorial((A - x)) * math.factorial(x))
        combB = math.factorial(
            B) / (math.factorial((B - (n - x))) * math.factorial((n - x)))
        combAB = math.factorial(
            AB) / (math.factorial((AB - n)) * math.factorial(n))

        return combA * combB / combAB
    return 0


def calculateHHyper(A: int, B: int, n: int):
    AB = A + B
    return n * (A / AB)


def calculateVarHyper(A: int, B: int, n: int):
    AB = A + B
    return n * (A*B / math.pow(AB, 2)) * ((AB - n) / (AB - 1))

# GEOMÉTRICA


def calculateProbGeo(p: float, x: int):
    if x >= 1:
        return math.pow((1 - p), (x - 1)) * p

    return 0


def calculateHGeo(p: float):
    return 1 / p


def calculateVarGeo(p: float):
    return (1 - p) / math.pow(p, 2)

# BINOMIAL NEGATIVA


def calculateProbNegBin(p: float, k: int, x: int):
    if x >= k:
        combXK = math.factorial(
            x-1) / (math.factorial((x - 1 - (k - 1))) * math.factorial((k - 1)))

        return combXK * math.pow(1 - p, x - k) * math.pow(p, k)
    return 0


def calculateHNegBin(p: float, k: int):
    return k * (1 / p)


def calculateVarNegBin(p: float, k: int):
    return k * ((1 - p) / math.pow(p, 2))

# POISSON


def calculateProbPoisson(lamb: float, x: int):
    if x >= 0:
        return math.exp(-lamb) * (math.pow(lamb, x) / math.factorial(x))
    return 0


print("Calculadora de distribuições típicas \n")
option = 0
stack = []

while option != 8:
    print("Selecione qual opção deseja: \n 1 - Distribuição Uniforme \n 2 - Distribuição Bernoulli \n 3 - Distribuição Binomial \n 4 - Distribuição Hipergeométrica \n 5 - Distribuição Geométrica \n 6 - Distribuição Binomial Negativa \n 7 - Distribuição Poisson \n 8 - Fechar o programa \n 9 - Somatória de todas as probabilidades.")
    option = int(input())

    if option == 1:
        print("Digite os parâmetros da função probabilidade da Distribuição Uniforme \nOBS: a, b, x. Ex: 1 13 2")
        INPUT = input().split(" ")
        a = float(INPUT[0])
        b = float(INPUT[1])
        x = int(INPUT[2])
        stack.append(calculateProbUni(a, b, x))
        print("Probabilidade =", stack[-1])
        print("Esperança =", calculateHUni(a, b))
        print("Variância =", calculateVarUni(a, b))
    elif option == 2:
        print("Digite os parâmetros da função probabilidade da Distribuição Bernoulli \nOBS: p: float, x: int. Ex: 0.653 4")
        INPUT = input().split(" ")
        p = float(INPUT[0])
        x = int(INPUT[1])
        stack.append(calculateProbBern(p, x))
        print("Probabilidade =", stack[-1])
        print("Esperança =", p)
        print("Variância =", calculateVarBern(p))
    elif option == 3:
        print("Digite os parâmetros da função probabilidade da Distribuição Binomial \nOBS: p: float, n: int, x: int. Ex: 0.383 5 3")
        INPUT = input().split(" ")
        p = float(INPUT[0])
        n = int(INPUT[1])
        x = int(INPUT[2])
        stack.append(calculateProbBin(p, n, x))
        print("Probabilidade =", stack[-1])
        print("Esperança =", calculateHBin(p, n))
        print("Variância =", calculateVarBin(p, n))
    elif option == 4:
        print("Digite os parâmetros da função probabilidade da Distribuição Hipergeométrica \nOBS: A, B, n, x. Ex: 39 13 5 2")
        INPUT = input().split(" ")
        A = int(INPUT[0])
        B = int(INPUT[1])
        n = int(INPUT[2])
        x = int(INPUT[3])
        stack.append(calculateProbHyper(A, B, n, x))
        print("Probabilidade =", stack[-1])
        print("Esperança =", calculateHHyper(A, B, n))
        print("Variância =", calculateVarHyper(A, B, n))
    elif option == 5:
        print("Digite os parâmetros da função probabilidade da Distribuição Geométrica \nOBS: p, x. Ex: 0.75 3")
        INPUT = input().split(" ")
        p = float(INPUT[0])
        x = int(INPUT[1])
        stack.append(calculateProbGeo(p, x))
        print("Probabilidade =", stack[-1])
        print("Esperança =", calculateHGeo(p))
        print("Variância =", calculateVarGeo(p))
    elif option == 6:
        print("Digite os parâmetros da função probabilidade da Distribuição Binomial Negativa \nOBS: p, k, x. Ex: 0.75 4 3")
        INPUT = input().split(" ")
        p = float(INPUT[0])
        k = int(INPUT[1])
        x = int(INPUT[2])
        stack.append(calculateProbNegBin(p, k, x))
        print("Probabilidade =", stack[-1])
        print("Esperança =", calculateHNegBin(p, k))
        print("Variância =", calculateVarNegBin(p, k))
    elif option == 7:
        print("Digite os parâmetros da função probabilidade da Distribuição Poisson \nOBS: lambda, x. Ex: 3 3")
        INPUT = input().split(" ")
        lamb = float(INPUT[0])
        x = int(INPUT[1])
        stack.append(calculateProbPoisson(lamb, x))
        print("Probabilidade =", stack[-1])
        print("Esperança =", lamb)
        print("Variância =", lamb)
    elif option == 8:
        print("Até mais!")
        break
    elif option == 9:
        print("Somatória de todas as probabilidades: ")
        print(sum(stack))
        stack = []
    else:
        print("Opção inválida, escolha uma opção entre 0 e 8!")

    print("Seguir com a próxima operação? \n1 - Sim \n2 - Não")
    continueOption = int(input())
    if continueOption == 2:
        break
