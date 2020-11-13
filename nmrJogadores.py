def nmrJogadores(maxPlayers):
    print("\n\nPara começarmos o RPGzito, defina a quantidade de jogadores!")
    print("(Quantidade minima necessária: 2)")
    print("(Quantidade maxima até o momento: 3)\n")

    while True:
        insert = input("Digite a quatidade de jogadores: ")

        try:
            players = int(insert)

            if (players >= 2) and (players <= maxPlayers):
                return players
            elif players < 2:
                print("\nA quantidade mínima é de 2 jogadores\n")
            else:
                print("\nA quantidade máxima de jogadores até o momento são de {} jogadores\n".format(maxPlayers))

        except:
            print("\nFavor, digitar somente numero inteiro!\n")