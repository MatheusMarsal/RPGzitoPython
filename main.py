from nmrJogadores import nmrJogadores
from nomePlayers import nomePlayers
from definirSequencia import definirSequencia
from almtrVtrPosicoes import almtrVtrPosicoes

maxPlayers = 20  # Alterar somente via 'script' --> define a quantidade maxima de jogadores ( por conta de ter \n
# personagens limitados no momento )


def main():
    players = nmrJogadores(maxPlayers)
    nickName = []
    d20s = []
    pos = []

    almtrVtrPosicoes(players, pos)

    nomePlayers(players, nickName, d20s)

    definirSequencia(players, pos, d20s)

    print("-=" * 10)

    i = 0

    while i < players:
        print(nickName[pos[i]], end='::')
        print(d20s[pos[i]])

        i += 1


main()
