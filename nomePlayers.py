from dado import dado

def nomePlayers(players, nicks, dado20):

    i = 1

    nicks.append(input("Digite o nome da primeira pessoa: "))
    dado20.append(dado(20))

    while (i < players):
        nicks.append(input("Digite o nome da proxima pessoa: "))
        dado20.append(dado(20))

        vrfcRepeticao = 1

        while (vrfcRepeticao):
            for count in range(i):
                if (dado20[i] == dado20[count]):
                    dado20[i] = dado(20)
                    vrfcRepeticao = 1
                    break

                vrfcRepeticao = 0

        i += 1

    i = 0

    while (i < players):
        print(nicks[i], end='::')
        print(dado20[i])

        i += 1