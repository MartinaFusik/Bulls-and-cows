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
            print(cara)
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

def num_control(a, b):
    '''Počítání cows and bulls'''
    a = str(a)
    b = str(b)
    for i in range(0, 4):
        for j in range(0, 4):
            if (i == j) and (a[i] == b[j]):
                global bull_count
                bull_count += 1
            elif (i != j) and (a[i] == b[j]):
                global cow_count
                cow_count += 1
            else:
                pass
#Hlavní funkce
# This is the main function
print("Hi there")
print(cara)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(cara)
player_num = 0
user_choice = True
while (user_choice):
    cow_count = 0
    bull_count = 0
    game_num = cislo_generator()
    score_counter = 0
    while (True):
        player_input()
        score_counter = score_counter + 1
        num_control(game_num, player_num)
        if (bull_count == 4):
            print("Skvělé, jsi vítěz!")
            print("Hru jsi dokončil na", str(score_counter), "pokusů")
            print("Chceš hrát znovu? Stiskni Y")
            print("Jestli chceš skončit, stiskni jakoukoli klávesu.")
            choice = input("Jak si se rozhodl?: ")
            if (choice == "y"):
                user_choice = True
            else:
                user_choice = False
            break
        else:
            print("cow_count", cow_count)
            print("bull_count", bull_count)
            cow_count = 0
            bull_count = 0
