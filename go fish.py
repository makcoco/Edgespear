# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 13:20:42 2019

@author: cocoMAK
"""
import random


cards = ['1', '1', '1','1','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6',
         '6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10','11',
         '11','11','11','12','12','12','12','13','13','13','13']



class player(object):
    def __init__(self,i):
        self.card = None
        self.i = i
        j = i


    def ask(self):
        print(" Choose a player you want to ask for card.")
        action = input("> ")

        if action == "player1" or "player2" or "player3" or "player4":
            print(f"You choose {action}.")
            return player.choose_card(self,action)

        else:
            print("You can't choose someone who didn't exit.")
            return player.ask(self)

    def go_fish(self):
        pass
    def choose_card(self,a):
        print(self.i)
        print(f"You have {who[self.i].card}.Which one do you want from {a}.")
        action = input("> ")
        print(who[self.i].card)

    def give_card(self):
        pass



def fapai():
    i = 0 
    player = []
    while i != 5:
        a =   random.randint(0,len(cards))
        card = cards.pop(a-1)
        player.append(card)
        i = i + 1
    return player

player1 = player(1)
player2 = player(2)
#player3 = player(3)
#player4 = player(4)
who = {1: player1, 2: player2,  # 3:player3,4:player4
               }

player1.card = fapai()

player1.ask()