import random

class Roulette:
    slot = ["kosong","kosong","kosong","kosong","kosong","peluru"]
    player = ["Player1","Player2"]

    def __init__(self) -> None:
        pass

    def mengacak(suit_player):
        print(f"{suit_player} memutar silinder Revolver")
        random.shuffle(Roulette.slot)
        Roulette.menembak(suit_player)

    def menembak(suit_player):
        print(f"{suit_player} Menembak\n")
        #print(f"{Roulette.slot[0]}\n")
        
    def jika(suit_player):
        if Roulette.slot[0] == "peluru":
            Roulette.berhenti(suit_player)
        else:
            Roulette.suit()

    def berhenti(suit_player):
        print(f"{suit_player} Kalah\n")
        Roulette.player.remove(suit_player)
        #print(Roulette.player)
        exit()
    
    def suit():
        suit_player = random.choice(Roulette.player)
        print(f"{suit_player} kalah suit")
        Roulette.mengacak(suit_player)
        Roulette.jika(suit_player)



print("""
                        RUSSIAN ROULETTE

adalah permainan Gambling yang mengisi 1 peluru dalam sebuah Revolver
Dan menaruk pelatuk ke kepala diri sendiri sesuai giliran.

""")
loop = True

while loop:
    ingin = input("Apakah anda ingin bermain? [y/n] \n> ").upper()
    if ingin == "Y":
        print("")
        Roulette.suit()
    elif ingin == "N":
        exit()
    else:
        print("Anda salah ketik")