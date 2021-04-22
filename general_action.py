from players import Player
class General:
    def __init__(self, cards, money):
        self.__cards=cards
        self.__money= money

    def gain_coin():
        return int(1)
    
    def foreign_help():
        return int(2)
    
    def player_strike(cards, name):
        if len(cards)==2:
            position=int(input("Which card do you want to turn around (Left=0 or Right=1)?"))
            print(cards[position])
            cards.pop(position)
            return cards
        else:
            print(cards[0])
            cards.pop(0)
            print(name, "lost the game")
            return cards