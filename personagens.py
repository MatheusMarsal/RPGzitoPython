from dado import dado
import time

def personagens(person):
    dano = 0
    danoCritico = 0

    if person == 0:
        dano = dado(6)
		
        print("\nDado mob: {}\n".format(dano))

        if (dano % 2 != 0):
            print("\nMob acertou {} de dano!\n".format(dano))
            return dano
        else:
            print("\nO golpe do mob foi tão fraquinho, que não causou dano!\n")
            return 0

    if person == 1:
        dano = dado(6)

        print("\nDado Arqueiro: {}\n".format(dano))

        if dano == 1:
            print("\nArqueiro, rapaz... Voce errou :P\n")
            return 0

        if (dano == 2) or (dano == 4) or (dano == 5):
            print("\nArqueiro, Voce acertou {} de dano :D\n".format(dano))
            return dano

        if dano == 3:
            dano = dano + dano
            print("\nArqueiro, Voce considerou a velocidade do vento e deu {} de dano :D\n".format(dano))
            return dano

        if dano == 6:
            danoCritico = dado(10)

            print("\nCritico Arqueiro: {}\n".format(danoCritico))

            if (danoCritico == 1) or (danoCritico == 10):
                print("\nArqueiro, Voce quase acertou um critico mas algo de errado nao deu certo\n")
                print("Entao voce so acertou {} de dano :P\n".format(dano))
                return dano

            dano = dano + danoCritico
            print("\nArqueiro, Voce acertou o critico muito certeiro\n")
            print("Entao voce acertou uma flechada no joelho e causou {} de dano :D\n".format(dano))
            return dano

    if person == 2:
        dano = dado(6)

        print("\nDado Mago: {}\n".format(dano))

        if dano == 3:
            print("\nMago, rapaz... Voce errou :P\n")
            return 0

        if (dano == 1) or (dano == 2) or (dano == 4) or (dano == 5):
            print("\nMago, Voce acertou {} de dano :D\n".format(dano))
            return dano

        if dano == 6:
            danoCritico = dado(6)

            dano = dano + danoCritico

            print("\nPrimeiro critico Mago: {}\n".format(danoCritico))

            time.sleep(0.5)

            danoCritico = dado(6)

            dano = dano + danoCritico

            print("\nSegundo critico Mago: {}\n".format(danoCritico))

            print("\nMago, Voce canalizou uma magia poderoza!\n")
            print("Entao voce acertou {} de dano :D\n".format(dano))
            return dano


    if person == 3:
        dano = dado(6)

        print("\nDado Guerreiro {}:\n".format(dano))

        if dano == 3:
            print("\nGuerreiro, rapaz... Voce errou :P\n")
            return 0

        if (dano == 1) or (dano == 2) or (dano == 4) or (dano == 5):
            print("\nGuerreiro, Voce acertou {} de dano :D\n".format(dano))
            return dano

        if dano == 6:
            danoCritico = dado(12)

            print("\nCritico Guerreiro: {}\n".format(danoCritico))

            dano = dano + danoCritico

            print("\nGuerreiro, Voce despertou sua furia interior!\n")
            print("Entao voce deu uma avuadora de quermece\n   Causando {} de dano :D\n".format(dano))
            return dano