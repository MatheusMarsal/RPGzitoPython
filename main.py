from nmrJogadores import nmrJogadores
from nomePlayers import nomePlayers
from definirSequencia import definirSequencia
from almtrVtrs import almtrVtrs
from escolhaPersonagem import escolhaPersonagem
from turnoBatalhas import turnoBatalhas

maxPlayers = 3  # Alterar somente via 'script' --> define a quantidade maxima de jogadores ( por conta de ter \n
# personagens limitados no momento )

def main():
    players = nmrJogadores(maxPlayers)
    nickName = []
    d20s = []
    pos = []
    personagens = []
    hp = []


    almtrVtrs(players, pos, personagens, hp)

    nomePlayers(players, nickName, d20s)

    definirSequencia(players, pos, d20s)

    print()
    print("-=" * 10)
    print()

    i = 0

    while i < players:
        print(nickName[pos[i]], end='::')
        print(d20s[pos[i]])

        i += 1

    escolhaPersonagem(players, nickName, pos, personagens, hp)

    turnoBatalhas(players, nickName, pos,personagens, hp)

main()
