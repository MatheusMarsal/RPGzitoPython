def definirSequencia(players, pos1, d20):
    pivod20 = []
    pos2 = []
    i = 0
    j = 0
    k = 0
    maior = 0



    for i in range(players):
        pivod20.append(d20[i])
        pos2.append(i)

    while True:
        maior = 0

        for i in range(players):
            if pivod20[i] > maior:
                maior = pivod20[i]
                j = i

        if maior == 0:
            break
        pivod20[j] = 0
        pos2[k] = j
        k += 1

    for i in range(players):
        pos1[i] = pos2[i]