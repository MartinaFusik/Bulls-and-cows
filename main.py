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

#Hrajeme
#porovnávání čísel
#Vyhodnocení
#Vyhrál x prohrál
#Hra začíná - hlavní funkce
print(
    "Hi there!",("\n"),
    cara,("\n"),
    "I've generated a random 4 digit number for you.",("\n"),
    "Let's play a bulls and cows game.",("\n"),
    cara)
hrac = input("Zadej 4 čísla:")
print(generuj_cislo())


