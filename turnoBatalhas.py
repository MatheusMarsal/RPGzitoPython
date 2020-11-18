from dado import dado
from personagens import personagens

def turnoBatalhas(players, nome, listaColocado, pers, life):
    posAtacante = 0
    posOponente = 0
    lado = 0
    vivo = []
    mortos = 0
    dano = []
    pivoDano = 0

    for i in range(players):
        vivo.append(1)

    for i in range(players):
        life[i] = 50

    for i in range(players):
        dano.append(0)

    while mortos != (players - 1):
        for i in range(players):
            if vivo[i] == 0:
                continue
            if life[i] <= 0:
                vivo[i] = 0
                mortos += 1

        if mortos == (players - 1):
            for i in range(players):
                if vivo[i]:
                    print("\n{} -> play!" .format(players))
                    print("\n{} -> mortos!" .format(mortos))
                    print("\n{}, voce sobreviveu a toda batalha".format(nome[listaColocado[i]]))
                    print("\nCom {} de HP" .format(life[i]))
                    print("\nDano causado na partida: {}" .format(dano[i]))
                    print("\nPARABENS!\n\n")

                    return

        if vivo[posAtacante]:

            posOponente = posAtacante

            lado = dado(2)

            if lado == 1:
                while (posAtacante == posOponente) or (posAtacante == players) or (vivo[posOponente] == 0):
                    posOponente -= 1

                    if posOponente < 0:
                        posOponente = players - 1

                print("\n{}, voce vai atacar {}, pela esquerda!".format(nome[listaColocado[posAtacante]], nome[listaColocado[posOponente]]))

                pivoDano = personagens(pers[posAtacante])

                dano[posAtacante] += pivoDano
                life[posOponente] -= pivoDano

                print("\n{} seu HP atual: {}".format(nome[listaColocado[posOponente]], life[posOponente]))



            if lado == 2:
                while (posAtacante == posOponente) or (posAtacante == -1) or (vivo[posOponente] == 0):
                    posOponente += 1

                    if posOponente >= players:
                        posOponente = 0


                print("\n{}, voce vai atacar {}, pela direita!\n".format(nome[listaColocado[posAtacante]], nome[listaColocado[posOponente]]))


                pivoDano = personagens(pers[posAtacante])

                dano[posAtacante] += pivoDano
                life[posOponente] -= pivoDano

                print("\n{} seu HP atual: {}".format(nome[listaColocado[posOponente]], life[posOponente]))

        posAtacante += 1

        if posAtacante == players:
            posAtacante = 0