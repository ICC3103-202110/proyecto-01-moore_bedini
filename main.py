import random
from general_action import General
from character_action import Character
from options import Options

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

    def money_player(challenger):
        if challenger == 1:
            return (Money_P1)
        elif challenger == 2:
            return (Money_P2)
        elif challenger == 3:
            return (Money_P3)
        elif challenger == 4:
            return (Money_P4)
    
    print("Welcome to Coup developed by Renzo bedini and Cristobal Moore") 
    num_players = int(input("How many players are going to play?: "))
    players=[]
    D = 'Duke'
    A = 'Assasin'
    C = 'Captain'
    E = 'Ambassador'
    CO = 'Contessa'

    deck = [D,A,C,E,CO]*3
    random.shuffle(deck)
    print(deck)
    Money_P1=2
    Money_P2=2
    Money_P3=2

    Cards_P1 = [ deck[0],deck[1] ]

    Cards_P2 = [ deck[2],deck[3] ]
    
    Cards_P3 = [ deck[4],deck[5] ]
    
    if num_players == 4:
        Cards_P4 = [ deck[6],deck[7] ]
        Money_P4=2
        
    deck = deck[-(15-(num_players)*2):]
    print(deck)
    while True:
        choose_1= input("Player 1, choose a general (write G) or character action (write C): ")            
        if choose_1 =='G':
            move=Options.menu_general_action()
            if move==1:
                Money_P1+=General.gain_coin()
                print(Money_P1)
            if move==2:
                block=Options.block_action(num_players)
                if block==0:
                    Money_P1+=General.foreign_help()
                    print(Money_P1)
                elif block !=0: 
                    decision = input("Do you want to challenge the player that blocked you? (YES or NO)")
                    if decision == 'YES':
                        player_x = player(block)
                        if 'Duke' in player_x:
                            Cards_P1 = delete_card(Cards_P1)
                        else:
                            player_x=delete_card(player_x)
            if move==3:
                if Money_P1>=7:
                    strike=Options.strike_action(num_players)
                    if strike==2:
                        General.player_strike(Cards_P2)
                    if strike==3:
                            General.player_strike(Cards_P3)
                    if strike==4:
                            General.player_strike(Cards_P4)
                    Money_P1= Money_P1-7
        if choose_1 == 'C':
            move=Options.menu_character_action()
            if move==1:
                challenger=Options.challenge_action(num_players)
                if challenger==0:
                    Money_P1+=Character.tax()
                    print(Money_P1)
                if challenger!=0:
                    if 'Duke' in Cards_P1:
                        position=Cards_P1.index('Duke')
                        print(Cards_P1[position])
                        player_x = player(challenger)
                        delete = delete_card(player_x)
                        Cards_P1,deck = new_card(deck,Cards_P1,position)
                        print(Cards_P1,deck)
                    else:
                        delete = delete_card(Cards_P1)
                
            if move==2:
                Money_P1=Money_P1-3
                challenger=Options.challenge_action(num_players)                  
                if challenger!=0:
                    if 'Assasin' in Cards_P1:
                        player_x = player(challenger)
                        player_x.pop(0)
                        player_x.pop(1)
                        print("Player", challenger, "has lost")
                    else:
                        Cards_P1 = delete_card(Cards_P1)
                block=Options.block_action(num_players)
                if block!=0:
                    decision = input("Do you want to challenge the player that blocked you? (YES or NO)")
                    if decision == 'YES':
                        player_x = player(block)
                        if 'Contessa' in player_x:
                            Cards_P1 = delete_card(Cards_P1)
                        else:
                            player_x.pop(0)
                            player_x.pop(1)
                            print("Player", block, "has lost")
                else:
                    strike=Options.strike_action(num_players)
                    player_x = player(strike)
                    murder = Character.murder(player_x)
            if move==3:
                challenger=Options.challenge_action(num_players)     
                if challenger!=0:
                    if 'Captain' in Cards_P1:
                        position=Cards_P1.index('Captain')
                        print(Cards_P1[position])
                        player_x = player(challenger)
                        delete = delete_card(player_x)
                        Cards_P1,deck = new_card(deck,Cards_P1,position)
                        print(Cards_P1,deck)
                    else:
                        Cards_P1=delete_card(Cards_P1)
                block=Options.block_action(num_players)
                if block!=0:
                    decision = input("Do you want to challenge the player that blocked you? (YES or NO)")
                    if decision == 'YES':
                        player_x = player(block)
                        if 'Ambassador' or 'Captain' in player_x:
                            Cards_P1 = delete_card(Cards_P1)
                            position=player_x.index('Captain' or 'Ambassador')
                            player_x,deck = new_card(deck,player_x,position)
                            print(Cards_P1,deck)
                        else:
                            player_x = delete_card(player_x)
                else:
                    stealing = Options.stealing_action(num_players)
                    money_x=money_player(steal)
                    Money_P1,money_x = Character.steal(Money_P1,money_x) 

            if move==4:
                challenger=Options.challenge_action(num_players)     
                if challenger!=0:
                    if 'Ambassador' in Cards_P1:
                        position=Cards_P1.index('Ambassador')
                        print(Cards_P1[position])
                        player_x = player(challenger)
                        delete = delete_card(player_x)
                        Cards_P1,deck = new_card(deck,Cards_P1,position)
                        print(Cards_P1,deck)
                    else:
                        Cards_P1=delete_card(Cards_P1)
                else:
                    Cards_P1,deck = Character.swap_cards(Cards_P1,deck)
                    


if __name__ == "__main__":
    main()