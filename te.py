# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 13:20:42 2019

@author: cocoMAK
"""
import random

# cards = ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6',
#          '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', '11',
#          '11', '11', '11', '12', '12', '12', '12', '13', '13', '13', '13']
cards = ['1', '1','2', '2','3', '3','4', '4','5', '5','6', '6',]
score = [0,0]
class player(object):
    def __init__(self, i):
        self.card = None
        self.i = i

    def ask(self):
        print(f"你是玩家{self.i}")
        for c in who[self.i].card:
            if who[self.i].card.count(c)==2:
                for x in who[self.i].card:
                    if x == c :
                        who[self.i].card.remove(x)
                score[self.i-1]+=1
        print("现在的比分是",score[0],":",score[1])
        print("现在手上有",self.card)
        print(" Choose a player you want to ask for card.")
        action = input("> ")

        if action == '1' or action == '2':
            print(f"You choose {action}.")
            return who[self.i].choose_card(action)

        else:
            print("You can't choose someone who didn't exit.")
            return who[self.i].ask()

    def go_fish(self):
        if len(cards)!=0:
            print("Go fish.")
            d = random.randint(0, len(cards))
            fish = cards.pop(d - 1)
            print(f"You got {fish}.")
            who[self.i].card.append(fish)
            print('还剩',len(cards),'张牌')
        else:
            print("pass")

    def pick_card(self):
        pass

    def choose_card(self, a):

        if a == str(self.i):
            print("你不能选自己")
            return self.ask()
            # j = 1
            # print(f"You have {who[self.i].card}.Which one do you want from {a}.")
            # action = input("> ")
            # return who[j].give_card(action,self.i)
        elif a != str(self.i):
            j = int(a)

            while True:
                print(f"You have {who[self.i].card}.Which one do you want from {a}.")
                action = input("> ")
                for e in self.card:
                    if action == e:
                        return who[j].give_card(action, self.i)
                print("你没有这张卡")


    def give_card(self, b, c):
        all = []
        for each in who[self.i].card:
            if each == b:
                all.append(each)
                who[self.i].card.remove(each)
               # who[c].card.extend(all)
        if who[self.i].card == None:
            who[self.i].card = fapai()
        if len(all)!=0:
            who[c].card.extend(all)
            print(f"给了{all}")
            print(player1.card,player2.card)
            return who[c].ask()
        else:
            return who[c].go_fish()


def fapai():
    i = 0
    player = []
    while i != 5:
        a = random.randint(0, len(cards))
        card = cards.pop(a - 1)
        player.append(card)
        i = i + 1
    return player

def start():
    i=1
    while ((len(cards)==0 )and (len(who[1].card)==0)and(len(who[2].card)==0))==0:
        who[i].ask()

        i = i % 2
        i = i + 1

    print("finish")
player1 = player(1)
player2 = player(2)
# player3 = player(3)
# player4 = player(4)
who = {1: player1, 2: player2,  # 3:player3,4:player4
       }

player1.card = fapai()
player2.card = fapai()
print(player1.card)
print(player2.card)
start()
#player1.ask()
print(player1.card)
# print(who[2].card)