from listaPersonagens import listaPersonagens


def escolhaPersonagem(players, nome, posicao, personagem, vida):

    listaPersonagens()

    inpt = 'str'
    i = 0

    while True:
        inpt = input("\n{} escolha seu personagem: ".format(nome[posicao[i]]))

        try:
            personagem[i] = int(inpt)

            nRepetiu = True

            if (personagem[i] > 0) and (personagem[i] <= 3):
                for j in range(i):
                    if personagem[i] == personagem[j]:
                        print("\nEsse personagem ja foi escolhido anteriormente!")
                        nRepetiu = False

                if nRepetiu:
                    print("\nEscolhido com sucesso!")
                    i += 1
                    nRepetiu = True
                if i > (players - 1):
                    break
            else:
                print("\nEste personagem ainda não existe!")
        except:
            print("\nFavor, digitar somente numero inteiro!")
