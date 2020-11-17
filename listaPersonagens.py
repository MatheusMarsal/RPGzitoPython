def listaPersonagens():
    # --> Arquerio
    print("\nDigite 1 para escolher --> Arquerio")
    print("\tUtiliza D6,D10 para dar dano")
    print("\t\t1 = Erra (nao acerta o alvo)")
    print("\t\t3 = Perfura a armadura do alvo causando o dobro do dano(6)")
    print("\t\t6 = Utiliza um D10, para uma nova rolagem de dano(sendo o minimo 0 e o maximo 9)")
    print("\t\t\tSe o d10 cair 1 ou 10, o alvo nao sofre dano adicional")

    # --> Mago
    print("\nDigite 2 para escolher --> Mago")
    print("\tUtiliza D6 para dar dano")
    print("\t\t3 = Erra!")
    print("\t\t6 = O primeiro dado o atinge o alvo e adiciona o dano de 2 D6!")

    # --> Guerreiro
    print("\nDigite 3 para escolher --> Guerreiro")
    print("\tUtiliza D6,D12 para dar dano")
    print("\t\t3 = Erra!")
    print("\t\t6 = O primeiro dado o atinge o alvo e adiciona o dano de um D12!")
