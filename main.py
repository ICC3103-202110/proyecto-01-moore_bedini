import random
from general_action import General
from character_action import Character
from print_options import Print_Option

def main():
    
    def delete_card(cards):
        position=int(input("Which card do you want to turn around (Left=0 or Right=1)?"))
        print(cards[position])
        cards.pop(position)
        return cards
    
    def player(challenger):
        if challenger == 1:
            return (Cards_P1)
        elif challenger == 2:
            return (Cards_P2)
        elif challenger == 3:
            return (Cards_P3)
        elif challenger == 4:
            return (Cards_P4)
    
    def new_card(deck,player,position):
        player.pop(position)
        deck.pop(0)
        random.shuffle(deck)
        player.append(deck[0])
        deck.pop(0)
        return player,deck

    print("Welcome to Coup developed by Renzo bedini and Cristobal Moore")
    num_players = int(input("How many players are going to play?: "))

    D = 'Duke'
    A = 'Assasin'
    C = 'Captain'
    E = 'Ambassador'
    CO = 'Contessa'

    deck = [D,A,C,E,CO]*3
    random.shuffle(deck)
    print(deck)
    Money_P1=5
    Money_P2=0
    Money_P3=0

    Cards_P1 = [ deck[0],deck[1] ]

    Cards_P2 = [ deck[2],deck[3] ]
    
    Cards_P3 = [ deck[4],deck[5] ]
    
    if num_players == 4:
        Cards_P4 = [ deck[6],deck[7] ]
        Money_P4=0
        
    deck = deck[-(15-(num_players)*2):]
    print(deck)
    while True:
        choose_1= input("Player 1, choose a general (write G) or character action (write C): ")            
        if choose_1 =='G':
            move=Print_Option.menu_general_action()
            if move==1:
                Money_P1+=General.gain_coin()
                print(Money_P1)
            if move==2:
                block=Print_Option.block_action(num_players)
                if block==0:
                    Money_P1+=General.foreign_help()
                    print(Money_P1)
            if move==3:
                if Money_P1>=7:
                    strike=Print_Option.strike_action(num_players)
                    if strike==2:
                        General.player_strike(Cards_P2)
                    if strike==3:
                            General.player_strike(Cards_P3)
                    if strike==4:
                            General.player_strike(Cards_P4)
                    Money_P1= Money_P1-7
        if choose_1 == 'C':
            move=Print_Option.menu_character_action()
            if move==1:
                challenger=Print_Option.challenge_action(num_players)
                block=Print_Option.block_action(num_players)
                if challenger==0 and block==0:
                    Money_P1+=Character.tax()
                if challenger!=0 and block==0:
                    if 'Duke' in Cards_P1:
                        position=Cards_P1.index('Duke')
                        print(Cards_P1[position])
                        player_x = player(challenger)
                        delete = delete_card(player_x)
                        Cards_P1,deck = new_card(deck,Cards_P1,position)

                        
                    




if __name__ == "__main__":
    main()