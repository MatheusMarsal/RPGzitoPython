from nmrJogadores import nmrJogadores
from random import randrange

maxJogadores = 3

nmrPlayers = nmrJogadores(maxJogadores)

jogadores = {}

'''
def dado(lados):
    d = (randrange(1, lados + 1))

    return d


def quickSort(nmrPessoas, pos1, d20):
    pivod20 = []
    pos2 = []
    i = 0
    j = 0
    k = 0
    maior = 0

    for i in range(nmrPessoas):
        pivod20.append(d20[i])
        pos2.append(i)

    while (True):
        maior = 0

        for i in range(nmrPessoas):
            if (pivod20[i] > maior):
                maior = pivod20[i]
                j = i

        if (maior == 0):
            break

        pivod20[j] = 0
        pos2[k] = j
        k += 1

    for i in range(nmrPessoas):
        pos1[i] = pos2[i]


def main():
    nmrPessoas = 0
    nmPessoas = []
    d20s = []
    pos = []
    i = 1
    j = 0
    vrfcRepeticao = 1
    houveRepeticao = 0
    nmrPessoas = int(input("Digite a quantidade de pessoas: "))

    nmPessoas.append(input("Digite o nome da primeira pessoa: "))
    d20s.append(dado(20))

    while (i < nmrPessoas):
        nmPessoas.append(input("Digite o nome da proxima pessoa: "))
        d20s.append(dado(20))

        vrfcRepeticao = 1
        houveRepeticao = 0

        while (vrfcRepeticao):
            for count in range(i):
                if (d20s[i] == d20s[count]):
                    d20s[i] = dado(20)
                    vrfcRepeticao = 1
                    break

                vrfcRepeticao = 0

        i += 1

    i = 0

    while (i < nmrPessoas):
        print(nmPessoas[i], end='::')
        print(d20s[i])

        i += 1

    for count in range(nmrPessoas):
        pos.append(count)

    quickSort(nmrPessoas, pos, d20s)

    print("-=" * 10)

    i = 0

    while (i < nmrPessoas):
        print(nmPessoas[pos[i]], end='::')
        print(d20s[pos[i]])

        i += 1


main()

'''