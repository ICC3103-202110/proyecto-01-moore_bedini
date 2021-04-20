import random
from general_action import General
from character_action import Character
from options import Options
from player import Player

def main():
    
    def delete_card(cards):
        position=int(input("Which card do you want to turn around (Left=0 or Right=1)?"))
        print(cards[position])
        cards.pop(position)
        return cards
    
    def player(challenger):
        if challenger == 1:
            return (players[0].cards)
        elif challenger == 2:
            return (players[1].cards)
        elif challenger == 3:
            return (players[2].cards)
        elif challenger == 4:
            return (players[3].cards)
    
    def new_card(deck,player,position):
        player.pop(position)
        deck.pop(0)
        random.shuffle(deck)
        player.append(deck[0])
        deck.pop(0)
        return player,deck

    def money_player(challenger):
        if challenger == 1:
            return (players[0].coins)
        elif challenger == 2:
            return (players[1].coins)
        elif challenger == 3:
            return (players[2].coins)
        elif challenger == 4:
            return (players[3].coins)
    
    print("Welcome to Coup developed by Renzo bedini and Cristobal Moore") 
    num_players = int(input("How many players are going to play?: "))
    D = 'Duke'
    A = 'Assasin'
    C = 'Captain'    
    E = 'Ambassador'    
    CO = 'Contessa'
    deck = [D,A,C,E,CO]*3
    random.shuffle(deck)
    players=Player.create_players(deck,num_players)
    print(players[0].name)
    print(deck)
    
    for i in range(num_players):
        print(players[i].cards)
        print(players[i].name, "choose a general (write G) or character action (write C): ")
        choose_1= input()            
        if choose_1 =='G':
            move=Options.menu_general_action()
            if move==1:
                players[i].coins+=General.gain_coin()
                print(players[i].coins)
            elif move==2:
                block=Options.block_action(num_players)
                if block==0:
                    players[i].coins+=General.foreign_help()
                elif block !=0: 
                    decision = input("Do you want to challenge the player that blocked you? (YES or NO)")
                    if decision == 'YES':
                        player_x = player(block)
                        if 'Duke' in player_x:
                            print(players[i].name, "lost the card for challenge the block")
                            players[i].cards = delete_card(players[i].cards)
                            print(players[i].cards)
                        else:
                            print(players[block-1].name, "lost a card for lying about the card")
                            player_x=delete_card(player_x)
                    else:
                        print(players[block-1].name,"block",players[i].name)
            elif move==3:
                if players[i].coins>=7:
                    strike=Options.strike_action(num_players)
                    General.player_strike(players[strike-1].cards)
                    print(players[i].name, "choose hit ",players[strike-1].name)
                    players[i].coins-=7
                    print(players[strike-1].name, "lost a card because a hit by ",players[i].name)

        elif choose_1 == 'C':
            move=Options.menu_character_action()
            if move==1:
                challenger=Options.challenge_action(num_players)
                if challenger==0:
                    players[i].coins+=Character.tax()
                    print(players[i].coins,"Gain 3 coins")
                if challenger!=0:
                    if 'Duke' in players[i].cards:
                        position=players[i].name.index('Duke')
                        print(players[i][position].cards)
                        player_x = player(challenger)
                        delete_card(player_x)
                        players[i].cards,deck = new_card(deck,players[i].cards,position)
                        print(players[challenger-1].name, "lost a card for challenge the action")
                    else:
                        delete_card(players[i].cards)
                        print(players[i].name, "lost a card for lying about the card")
    
            if move==2:
                players[i].coins-=3
                challenger=Options.challenge_action(num_players)                  
                if challenger!=0:
                    if 'Assasin' in players[i].cards:
                        player_x = player(challenger)
                        delete_card(player_x)
                        print(players[challenger-1].name, "lost a card for challenge the action")
                    else:
                        delete_card(players[i].cards)
                        print(players[i].name, "lost a card for lying about the card")
                strike=Options.strike_action(num_players)
                print(players[strike-1].name, "do you want to block the player that murder you? (YES or NO)")
                decision = input()
                if decision == 'YES':
                    print(players[i].name, "do you want to challenge the player that block you? (YES or NO)")
                    decision2 = input()
                    if decision2 == 'YES':
                        player_x = player(strike)
                        if 'Contessa' in player_x:
                            delete_card(players[i].cards)
                            print(players[i].name, "lost a card for challenge the action")
                        else:
                            players[strike-1].cards.pop(0)
                            players[strike-1].cards.pop(1)
                            print(players[challenger-1].name, "has lost the game")
                else:
                    player_x = player(strike)
                    murder = Character.murder(player_x)
                    print(players[i].name, "murder", players[strike-1].name)

                
                if block!=0:
                    decision = input("Do you want to challenge the player that blocked you? (YES or NO)")
                    if decision == 'YES':
                        player_x = player(block)
                        if 'Contessa' in player_x:
                            delete_card(players[i].cards)
                            print(players[i].name, "lost a card for challenge the action")
                        else:
                            delete_card(player_x)
                            print(players[challenger-1].name, "lost a card for lying about the card")
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
                    
    
             


                    




if __name__ == "__main__":
    main()