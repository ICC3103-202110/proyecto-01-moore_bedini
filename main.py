import random
from general_action import General
from character_action import Character
from options import Options
from players import Player

def main():
    
    def delete_card(cards):
        if len(cards)==2:
            position=int(input("Which card do you want to turn around (Left=0 or Right=1)?"))
            print(cards[position])
            cards.pop(position)
            return cards
        else:
            cards.pop(0)
            print(cards[0])
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
    deck = ['Duke','Assasin','Captain','Ambassador','Contessa']*3
    random.shuffle(deck)
    players=Player.create_players(deck,num_players)
    print(deck)
    players_alive = num_players
    while players_alive!=1:
        for i in range(num_players):
            if len(players[i].cards)>0:
                print(players_alive)  
                print(players[i].name, "do you want to see your cards? (YES or NO) ")
                answer = input()
                if answer == 'YES':
                    print(players[i].cards)
                print(players[i].name, "choose a general (write G) or character action (write C): ")
                choose_1= input() 
                if choose_1 =='G':
                    move=Options.menu_general_action()
                    if move==1:
                        players[i].coins+=General.gain_coin()
                        print(players[i].coins)
                    elif move==2:
                        block=Options.block_action(num_players,players,i)
                        if block==-1:
                            players[i].coins+=General.foreign_help()
                            print(players[i].coins)
                            print(players[i].name, "Gain two coins")
                        elif block !=-1: 
                            decision = input("Do you want to challenge the player that blocked you? (YES or NO)")
                            if decision == 'YES':
                                player_x = player(block+1)
                                if 'Duke' in player_x:
                                    position=player_x.index('Duke')
                                    print(player_x[position])
                                    player_x,deck = new_card(deck,player_x,position)
                                    players[i].cards=delete_card(players[i].cards)
                                    if len(players[i].cards)==0:  
                                        print(players[i].name, "lost the card for challenging the block")
                                        print(players[i].name, "lost the game")

                                else:
                                    player_x=delete_card(player_x)
                                    if len(player_x)==0:  
                                        print(players[block].name, "lost the card for challenging the block")
                                        print(players[block].name, "lost the game")
                            else:
                                print(players[block].name,"block",players[i].name)
                    elif move==3:
                        if players[i].coins>=7:
                            players[i].coins-=7
                            strike=Options.strike_action(num_players, players, players[i].name)
                            General.player_strike(players[strike].cards)
                            if len(players[strike].cards)==0:
                                print(players[i].name, "chooses to hit ",players[strike].name)
                                print(players[strike].name, "lost a card because he got hit by ",players[i].name)
                                print(players[strike].name, "lost the game")
                            else:
                                print(players[i].name, "chooses to hit ",players[strike].name)
                                print(players[strike].name, "lost a card because he got hit by ",players[i].name)

                elif choose_1 == 'C':
                    move=Options.menu_character_action()
                    if move==1:
                        challenger=Options.challenge_action(num_players)
                        if challenger==-1:
                            players[i].coins+=Character.tax()
                            print(players[i].name,"gains 3 coins")
                        elif challenger!=-1:
                            if 'Duke' in players[i].cards:
                                position=players[i].cards.index('Duke')
                                print(players[i].cards[position])
                                players[i].cards,deck = new_card(deck,players[i].cards,position)
                                player_x = player(challenger+1)
                                delete_card(player_x)
                                if len(players[challenger].cards)==0:  
                                    print(players[challenger].name, "lost the card for challenging")
                                    print(players[challenger].name, "lost the game")
                                else:
                                    print(players[challenger].name, "lost a card for challenging the action")
                                    players[i].coins+=Character.tax()
                                    print(players[i].name,"gains 3 coins")
                            else:
                                delete_card(players[i].cards)
                                if len(players[i].cards)==0:  
                                        print(players[i].name, "lost the card for lying about the card")
                                        print(players[i].name, "lost the game")
                                else:
                                    print(players[i].name, "lost a card for lying about the card")
                    elif move==2:
                        if players[i].coins>=3:
                            players[i].coins-=3
                            challenger=Options.challenge_action(num_players,players,i)                  
                            if challenger!=-1:
                                if 'Assasin' in players[i].cards:
                                    position=players[i].cards.index('Assasin')
                                    print(players[i].cards[position])
                                    players[i].cards,deck = new_card(deck,players[i].cards,position)
                                    player_x = player(challenger+1)
                                    delete_card(player_x)
                                    if len(players[challenger].cards)==0:  
                                        print(players[challenger].name, "lost the card for challenging")
                                        print(players[challenger].name, "lost the game")
                                    else:
                                        print(players[challenger].name, "lost a card for challenging the action")
                                else:
                                    delete_card(players[i].cards)
                                    if len(players[i].cards)==0:  
                                        print(players[i].name, "lost the card for challenging")
                                        print(players[i].name, "lost the game")
                                    else:
                                        print(players[i].name, "lost a card for lying about the card")       
                            strike=Options.strike_action(num_players,players, players[i].name)
                            print(players[strike].name, "do you want to block the player that wants to kill you? (YES or NO)")
                            decision = input()
                            if decision == 'YES':
                                print(players[i].name, "do you want to challenge the player that blocked you? (YES or NO)")
                                decision2 = input()
                                if decision2 == 'YES':
                                    player_x = player(strike)
                                    if 'Contessa' in player_x:
                                        position=player_x.index('Contessa')
                                        print(player_x[position])
                                        player_x,deck = new_card(deck,player_x,position)
                                        delete_card(players[i].cards)
                                        if len(players[i].cards)==0:  
                                            print(players[i].name, "lost the card for challenging")
                                            print(players[i].name, "lost the game")
                                        else:
                                            print(players[i].name, "lost a card for challenging the action")
                                    else:
                                        if len(players[strike].cards)==2:
                                            players[strike].cards.pop(0)
                                            players[strike].cards.pop(0)
                                            print(players[i].name, "assasinated", players[strike].name)
                                            print(players[strike].name, "has lost the game")
                                        else:
                                            players[strike].cards.pop(0)
                                            print(players[i].name, "assasinated", players[strike].name)
                                            print(players[strike].name, "has lost the game")
                            else:
                                player_x = player(strike)
                                Character.murder(player_x)
                                if len(players[strike].cards)==0:  
                                    print(players[i].name, "assasinated", players[strike].name)
                                    print(players[strike].name, "lost the game")
                                else:
                                    print(players[i].name, "assasinated", players[strike].name)
                
                    if move==3:
                        challenger=Options.challenge_action(num_players)     
                        if challenger!=-1:
                            if 'Captain' in players[i].cards:
                                position=players[i].cards.index('Captain')
                                print(players[i].cards[position])
                                players[i].cards,deck = new_card(deck,players[i].cards,position)
                                player_x = player(challenger+1)
                                delete_card(player_x)
                                if len(players[challenger].cards)==0:  
                                        print(players[challenger].name, "lost the card for challenging")
                                        print(players[challenger].name, "lost the game")
                                else:
                                    print(players[challenger].name, "lost a card for challenging")
                            else:
                                delete_card(players[i].cards)
                                if len(players[i].cards)==0:  
                                        print(players[i].name, "lost the card for lying about the card")
                                        print(players[i].name, "lost the game")
                                else:
                                    print(players[i].name, "lost the card for lying about the card")
                        steal = Options.stealing_action(num_players)
                        print(players[steal].name, "do you want to block the player that wants to steal from you? (YES or NO) ")
                        decision = input()
                        if decision == 'YES':
                            print(players[i].name, "do you want to challenge the player that blocked you? (YES or NO)")
                            decision2 = input()
                            if decision2 == 'YES':
                                player_x = player(steal+1)
                                if 'Ambassador' in player_x:
                                    position=player_x.index('Ambassador')
                                    print(player_x[position])
                                    player_x,deck = new_card(deck,player_x,position)
                                    delete_card(players[i].cards)
                                    if len(players[i].cards)==0:  
                                        print(players[i].name, "lost the card for challenging")
                                        print(players[i].name, "lost the game")
                                    else:
                                        print(players[i].name, "lost a card for challenging the action")
                                
                                elif 'Captain' in player_x:
                                    position=player_x.index('Captain')
                                    print(player_x[position])
                                    player_x,deck = new_card(deck,player_x,position)
                                    delete_card(players[i].cards)
                                    if len(players[i].cards)==0:  
                                        print(players[i].name, "lost the card for challenging")
                                        print(players[i].name, "lost the game")
                                    else:
                                        print(players[i].name, "lost a card for challenging")
                                else:
                                    player_x = delete_card(player_x)
                                    if len(players[steal].cards)==0:  
                                        print(players[steal].name, "lost the card for challenging")
                                        print(players[steal].name, "lost the game")
                                    else:
                                        print(players[steal].name, "lost the card for lying")
                            else:
                                money_x=money_player(steal)
                                players[i].coin,players[steal-1].coins = Character.steal(players[i].coins,players[steal-1].coins)
                                print(players[i].name, "stole coins from", players[steal-1].name)
                        else:
                            money_x=money_player(steal+1)
                            players[i].coin,money_x = Character.steal(players[i].coins,money_x) 
                            print(players[i].name, "stole coins from", players[steal].name)


                    if move==4:
                        challenger=Options.challenge_action(num_players)     
                        if challenger!=-1:
                            if 'Ambassador' in players[i].cards:

                                position=players[i].cards.index('Ambassador')
                                print(players[i].cards[position])
                                players[i].cards,deck = new_card(deck,players[i].cards,position)
                                player_x = player(challenger+1)
                                delete_card(player_x)
                                if len(players[challenger].cards)==0:  
                                        print(players[challenger].name, "lost the card for challenging")
                                        print(players[challenger].name, "lost the game")
                                else:
                                    print(players[challenger-1].name, "lost a card for challenging")
                            else:
                                delete_card(players[i].cards)
                                if len(players[i].cards)==0:  
                                        print(players[i].name, "lost a card for lying")
                                        print(players[i].name, "lost the game")
                                else:
                                    print(players[i].name, "lost a card for lying")
                        else:
                            players[i].cards,deck = Character.swap_cards(players[i].cards,deck)
                            print(players[i].name, "swaped two cards from the deck")
            else:
                players_alive = players_alive - 1                    

if __name__ == "__main__":
    main()