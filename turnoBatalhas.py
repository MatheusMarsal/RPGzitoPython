from dado import dado
from personagens import personagens
from clear import clear
import random

def pause():
    input("\nPressione enter para continuar...\n")

def randMob(players, nomes, listaColocado, personagem, vida):
    mobs = ["goblin", "aranha grande", "ratão de buero", "lobo selvagem", "gato com faca nas coxtaz", "Serpente", "lagarto", "javali", "slime"]

    j = players

    for i in range(players, 0 , -1):
        listaColocado.insert(i, j)
        j += 1

        personagem.append(0)
        vida.append(dado(10))

    for count in range((players), 0, -1):
        mob = random.choice(mobs)
        nomes.append(mob)


def hpBar(hp):
    red = "\033[1;31m"
    green = "\033[1;32m"
    grey = "\033[1;90m"
    blue = "\033[1;94m"
    reset = "\033[0;0m"

    print(grey + "[", end='')
    for i in range(50):
        if i < hp:
            print(green + "+", end='')
        else:
            print(red + "-", end='')

    print(grey + "]", blue + "-->", end='')

    if hp > 0:
        print(green, hp, reset)
    else:
        print(red, "Faleceu!", reset)

def turnoBatalhas(players, nome, listaColocado, pers, life):
    posAtacante = 0
    posOponente = 0
    lado = 0
    vivo = []
    mortos = 0
    dano = []
    pivoDano = 0
	

    for i in range(players * 2):
        vivo.append(1)

    for i in range(players):
        life[i] = 50

    for i in range(players * 2):
        dano.append(0)

    players = players * 2

    randMob(players, nome, listaColocado, pers, life)

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
                    print("\n\n{}, voce sobreviveu a toda batalha".format(nome[listaColocado[i]]))
                    print("\n{} seu HP atual: ".format(nome[listaColocado[i]]), end='')
                    hpBar(life[i])
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
                pause()

                pivoDano = personagens(pers[posAtacante])

                dano[posAtacante] += pivoDano
                life[posOponente] -= pivoDano

                print("\n{} seu HP atual: ".format(nome[listaColocado[posOponente]]), end='')
                hpBar(life[posOponente])

                pause()

                clear()



            if lado == 2:
                while (posAtacante == posOponente) or (posAtacante == -1) or (vivo[posOponente] == 0):
                    posOponente += 1

                    if posOponente >= players:
                        posOponente = 0



                print("\n{}, voce vai atacar {}, pela direita!\n".format(nome[listaColocado[posAtacante]], nome[listaColocado[posOponente]]))
                pause()


                pivoDano = personagens(pers[posAtacante])

                dano[posAtacante] += pivoDano
                life[posOponente] -= pivoDano

                print("\n{} seu HP atual: ".format(nome[listaColocado[posOponente]]), end='')
                hpBar(life[posOponente])

                pause()
				
                clear()

        posAtacante += 1

        if posAtacante == players:
            posAtacante = 0