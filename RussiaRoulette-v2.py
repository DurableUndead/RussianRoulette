import random

class Roulette:
    slot = ['kosong','kosong','kosong','kosong','kosong','peluru']
    player = ['Player1','Player2']

    def __init__(self) -> None:
        # self.suit()
        # self.mengacak()
        # self.menembak()
        # self.jika()
        # self.berhenti()
        pass
        
    def mengacak(self, suit_player):
        print(f'{suit_player} memutar silinder Revolver')
        random.shuffle(self.slot)
        self.menembak(suit_player)

    def menembak(self, suit_player):
        print(f'{suit_player} Menembak\n')
        #print(f'{Roulette.slot[0]}\n')
        
    def jika(self, suit_player):
        if self.slot[0] == 'peluru':
            self.berhenti(suit_player)
        else:
            self.suit()

    def berhenti(self, suit_player):
        print(f'{suit_player} Kalah\n')
        self.player.remove(suit_player)
        #print(self.player)
        exit()
    
    def suit(self):
        suit_player = random.choice(self.player)
        print(f'{suit_player} kalah suit')
        self.mengacak(suit_player)
        self.jika(suit_player)



print("""
                        RUSSIAN ROULETTE

adalah permainan Gambling yang mengisi 1 peluru dalam sebuah Revolver
memutar secara cepat dan menaruk pelatuk ke kepala diri sendiri sesuai giliran.

""")

Roulette().suit()
# loop = True

# while loop:
#     ingin = input('Apakah anda ingin bermain? [y/n] \n> ').upper()
#     if ingin == 'Y':
#         print('')
#         Roulette.suit()
#     elif ingin == 'N':
#         exit()
#     else:
#         print('Anda salah ketik')