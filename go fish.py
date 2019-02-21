# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 13:20:42 2019

@author: cocoMAK
"""
import random
from textwrap import dedent

cards = ['1', '1', '1','1','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6',
         '6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10','11',
         '11','11','11','12','12','12','12','13','13','13','13']

class player(object):
    def __init__(self):
        self.card = None


class Ask(object):
    def enter(self):
        print(" Choose a player you want to ask for card.")
        action = "> "

        if action != "player1" or "player2" or "player3" or "player4":
            print("You can't choose someone who didn't exit.")
            return 'ask'

        elif action == "player1" or "player2" or "player3" or "player4":
            print(f"You choose {action}.",action)
            return 'choose_card'


class GoFish(object):
    def enter(self):
        pass


class ChooseCard(object):
    def enter(self):
        pass

class Finished(object):
    def enter(self):
        pass

class Action(object):
    move = {
        'ask': Ask(),
        'go_fish': GoFish(),
        'choose_card': ChooseCard(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Action.move.get(scene_name)
        return val


    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


def fapai():
    i = 0 
    player = []
    while i != 5:
        a =   random.randint(0,len(cards))
        card = cards.pop(a-1)
        player.append(card)
        i = i + 1
    return player


player1 = player()
player1.card = fapai()

a_map = Action('ask')
a_game = Engine(a_map)
a_game.play()