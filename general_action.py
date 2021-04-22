from players import Player
class General:
    def __init__(self, cards, money):
        self.__cards=cards
        self.__money= money

    def gain_coin():
        return int(1)
    
    def foreign_help():
        return int(2)
    
    def player_strike(cards, name, cards_players_lost):
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
                return cards
                cards.pop(0)
                return cards
