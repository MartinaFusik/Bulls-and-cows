"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Martina Fúsiková
email: martina.fusikova@gmail.com
discord: Martina_F#2319
"""
import random

cara = 47 * "-"

#Generování tajných číslic
def generuj_cislo():
    tajne_cislo = range(1000, 10000)
    unikatni_cislo = set(random.sample(tajne_cislo, 1))
    return unikatni_cislo

#vstup od uživatele

def kontrola_vstupu(cisla: str):
    '''Kontroluje čísla ze vstupu od uživatele.
    Číslo musí být jen číslo a zároveň se hodnoty ve str
    nesmějí opakovat'''

    zkontrolovany_vstup = []
    for i in cisla:
        if i not in zkontrolovany_vstup:
            if i.isdigit() == True:
                var = len(zkontrolovany_vstup) > 4
                zkontrolovany_vstup.append(i)
                if var is False:
                    print("Zadej 4 čísla.")
            else:
                print("Zadej jen čísla!")
        else:
            print("Čísla se nemohou opakovat. Zadej jinou kombinaci.")
    return zkontrolovany_vstup

def vstup_s_nulou(cisla: list):
    '''Kontrolovaný vstup od uživatele nesmí začínat číslem: 0'''

    if cisla[0] != "0":
        pass
    else:
        print("Číslo nesmí začínat 0")

def porovnavani(hrac,pocitac):
    bull_cow = [0, 0]
    hrac_li = kontrola_vstupu(hrac)
    for i,j in zip(hrac_li, pocitac):
        if j in hrac_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

#Hrajeme
def hrajeme(hrac, pocitac):
    while hrac == pocitac:
        bull_cow = porovnavani(hrac, pocitac)
        print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
        if bull_cow[0] == 4:
            print("You guessed right!")

#porovnávání čísel
#Vyhodnocení
#Vyhrál x prohrál
#Hra začíná - hlavní funkce
def main():
    print(
    "Hi there!",("\n"),
    cara,("\n"),
    "I've generated a random 4 digit number for you.",("\n"),
    "Let's play a bulls and cows game.",("\n"),
    cara)
    hrac = input("Zadej 4 čísla:")
    pocitac = generuj_cislo()

    while hrac != pocitac:
        dalsi_moznost = input(">>>")
        porovnavani(dalsi_moznost, pocitac)
        hrajeme(hrac, pocitac)
        print(f"{dalsi_moznost[0]} bulls, {dalsi_moznost[1]} cows")
        if hrac == pocitac:
            print("Vyhrál si!")



main()





