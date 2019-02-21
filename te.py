import random

cards = ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6',
        '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', '11',
         '11', '11', '11', '12', '12', '12', '12', '13', '13', '13', '13']
class player(object):
    def __init__(self):
        self.card = None
    def go_fish():
        pass
    def ask():
        pass

def fapai():

    player = []
    for i in range(0,5):
        a = random.randint(0,len(cards))
        card = cards.pop(a -1 )
        player.append(card)
    return player
player1=player()
player1.card=fapai()

print(player1.card,
      #"\n",player2.card,'\n',player3.card,'\n',player4.card,'\n',
        cards)