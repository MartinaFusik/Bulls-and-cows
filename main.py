"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Martina Fúsiková
email: martina.fusikova@gmail.com
discord: Martina_F#2319
"""
import random

cara = 47 * "-"


# Generování tajných číslic
def cislo_generator():
    '''Generování náhodných čísel pro hru bez 0 na začátku a opakujících čísel'''
    gen_cislo = [0]
    while gen_cislo[0] == 0:
        gen_cislo = random.sample(range(0, 10), 4)
    return ("".join(map(str, gen_cislo)))


# vstup od uživatele
def player_input():
    '''Kontrola počtu zadaných čísel'''
    while (True):
        try:
            global player_num
            z = player_num = input("Enter a number:")
            z = int(z[0])
            '''Kontrola, zda číslo začíná 0'''
            if z == 0:
                print("Číslo nesmí začínat 0")
                continue
            '''Kontrola 4 zadaných čísel'''
            if (len(player_num) != 4):
                print("Vlož pouze 4 čísla!")
                continue
        except ValueError:
            '''Kontrola zda obsahuje písmena'''
            print("Vlož pouze číslice!")
        else:
            x = 0
            for i in range(0, 4):
                x = x + player_num.count(player_num[i])
            '''Kontrola, zda se číslo neopakuje'''
            if (x != 4):
                print("Vlož čísla, která se neopakují")
                continue
            else:
                return

def porovnavani(hrac, pocitac):
    hrac = player_num
    bull_cow = [0, 0]
    for i, j in zip(hrac, pocitac):
        if j in hrac:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

# Hra začíná - hlavní funkce
print(
    "Hi there!", ("\n"),
    cara, ("\n"),
    "I've generated a random 4 digit number for you.", ("\n"),
    "Let's play a bulls and cows game.", ("\n"),
    cara)

player_num = str(0)
user_choice = True
while (user_choice):
    cow_count = 0
    bull_count = 0
    game_num = generuj_cislo()
    print(game_num)

    while (True):
        kontrola_vstupu()
        porovnavani(game_num, player_num)
        if (bull_count == 4):
            print("YOU WON")
            print("YOU HAVE COMPLETED THE GAME")
        else:
            print("cow_count", cow_count)
            print("bull_count", bull_count)
            cow_count = 0
            bull_count = 0
