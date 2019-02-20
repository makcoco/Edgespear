# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 13:20:42 2019

@author: cocoMAK
"""
import random
#fdasfjalsfjalfjl;aksfjas

cards = ['1','1','1','1','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6',
         '6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10','11',
         '11','11','11','12','12','12','12','13','13','13','13']

class player(object):
    card = []
    def __init__(self,card):
        self.card = card
    def go_fish():
        pass
    def ask():
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

player1 = player(fapai())
player2 = player(fapai())
player3 = player(fapai())
player4 = player(fapai())
print(player1.card)
print(player2.card)
print(player3.card)
print(player4.card)
print(cards)
