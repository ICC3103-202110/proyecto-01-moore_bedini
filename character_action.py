import random
import random
from players import Player
class Character:
    def __init__(self,cards):
        self.__cards = cards

    def tax():
        return int(3)
    
    def murder(cards, name, cards_players_lost):
        if len(cards)==2:
            position=int(input("Which card do you want to turn around (Left=0 or Right=1)?"))
            print(cards[position])
            if name not in cards_players_lost:
                cards_players_lost.append(name)
                cards_players_lost.append(cards[position])
                cards.pop(position)
                return cards
            else:
                visible_name = cards_players_lost.index(name)
                cards_players_lost.insert(visible_name+1, cards[position])
                return cards
            
        else:
            if name not in cards_players_lost:
                cards_players_lost.append(name)
                cards_players_lost.append(cards[0])
                cards.pop(0)
                return cards
            else:
                visible_name = cards_players_lost.index(name)
                cards_players_lost.insert(visible_name+1, cards[0])
                cards.pop(0)
                return cards
        
    def steal(Money,Money_x):
        if Money_x>=2:
            Money+=2
            Money_x-=2
        else:
            Money+=1
            Money_x-=1
        return Money,Money_x

    def swap_cards(cards,deck):
        cards.append(deck[0])
        cards.append(deck[1])
        deck.pop(0)
        deck.pop(1)
        print(cards)
        card_1 = input("First card you don't want to keep? For example: Duke, Captain, etc... ")
        position = cards.index(card_1)
        cards.pop(position)
        deck.append(card_1)
        card_2 = input("Second card you don't want to keep? For example: Duke, Captain, etc... ")
        position = cards.index(card_2)
        cards.pop(position)
        deck.append(card_2)
        random.shuffle(deck)
<<<<<<< HEAD
        print(cards)
        return cards, deck
    
=======
        print(cards,deck)
        return cards, deck
>>>>>>> 2d66802c0b4bb46a77f94b8380b3899950001fde
