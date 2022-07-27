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
    unikatni_cislo = random.sample(tajne_cislo, 1)
    return unikatni_cislo

#vstup od uživatele

def kontrola_vstupu(cisla: str):
    zkontrolovany_vstup = []
    for i in cisla:
        if i not in zkontrolovany_vstup:
            if i.isdigit() == True:
                zkontrolovany_vstup.append(i)
            else:
                print("Zadej jen čísla!")
        else:
            print("Čísla se nemohou opakovat. Zadej jinou kombinaci.")
    return zkontrolovany_vstup

def vstup_s_nulou(cisla: list):
    if cisla[0] != "0":
        pass
    else:
        print("Číslo nesmí začínat 0")


#Hrajeme
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
    vstup_s_nulou(kontrola_vstupu(hrac))

main()



