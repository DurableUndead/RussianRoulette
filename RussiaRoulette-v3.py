import random
import time

class Roulette:
    slot    = ['kosong','kosong','kosong','kosong','kosong','kosong','peluru']
    player  = ['Player#1','Player#2']
    waktu   = 1

    def __init__(self) -> None:
        pass
    
    def turn(self):
        giliran = random.choice(self.player)
        if giliran == self.player[0]:
            print(f"\n >>> {self.player[0]} jalan Pertama")
            self.shuffle()
            self.player1()
        else:
            print(f"\n >>> {self.player[1]} jalan duluan")
            self.shuffle()
            self.player2()

    def shuffle(self):
        random.shuffle(self.slot)
        print(f'\n >>> Silinder Revolver sedang diputar\n')
        print(f" >>> Game akan dimulai\n")
        time.sleep(self.waktu + 2)

    def player1(self):
        nama = self.player[0]
        self.shoot(nama)
        self.player2()

    def player2(self):
        nama = self.player[1]
        self.shoot(nama)
        self.player1()

    def shoot(self, nama):
        print(f'\n{nama} Menembak')
        self.condition(nama)

    def condition(self, nama):
        if self.slot[0] == 'peluru':
            del self.slot[0]
            self.stop(nama)
        else:
            del self.slot[0]
            print("\n>>> StandBy")
            time.sleep(self.waktu)

    def stop(self, nama):
        print(f'\n\n\n      {nama} Kalah (Mati)     \n\n\n')
        exit()


print("""
                        RUSSIAN ROULETTE

adalah permainan Gambling yang mengisi 1 peluru dalam sebuah Revolver
memutar secara cepat dan menaruk pelatuk ke kepala diri sendiri sesuai giliran.

""")
# Beretta
# Colt King Cobra
# Colt Paterson
# Colt Python
# Kort Combat
# Magnum
# Nagant M1895
# Remington M1858
# Smith & Wesson .38/44

Roulette().turn()
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