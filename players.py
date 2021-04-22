import random

class Player:
    
    def __init__ (self,name,coins,cards):
        self.name=name
        self.coins=coins
        self.cards=cards
        
    def create_players(deck, number):
        players=[]
        for i in range(number):
            players.append(Player('Player'+str(i+1),2,[deck[0],deck[1]]))
            deck.pop(0)
            deck.pop(0)
        return players
    
    