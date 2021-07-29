from random import randint
from os import system
from time import sleep
from art import diceFaces


def roll():
    for i in range(6):
        print(diceFaces[i])
        sleep(0.17)
        system("cls")
    val = randint(0, 5)
    print(diceFaces[val])

    return val+1
