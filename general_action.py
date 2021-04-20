class General:
    def __init__(self,cards,money):
        self.__cards=cards
        self.__money= money

    def gain_coin(self):
        return int(1)
    
    def foreign_help(self):
        return int(2)
    
    def player_strike(cards):
        position=int(input("Which card do you want to turn around (Left=0 or Right=1)?"))
        print(cards[position])
        cards.pop(position)
        return cards
