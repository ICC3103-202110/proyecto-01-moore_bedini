import random
from general_action import General
from character_action import Character
from options import Options
from players import Player

def main():
    def add_visible_card(position, cards, name, cards_players_lost):
        if name not in cards_players_lost:
            cards_players_lost.append(name)
            cards_players_lost.append(cards[position])
        else:
            visible_name = cards_players_lost.index(name)
            cards_players_lost.insert(visible_name+1, cards[position])
            

    def delete_card(cards, name, cards_players_lost):
        if len(cards)==2:
            position=int(input("Which card do you want to turn around (Left=0 or Right=1)?"))
            print(cards[position])
            add_visible_card(position, cards, name, cards_players_lost)
            cards.pop(position)
            return cards
        else:
            add_visible_card(0, cards, name, cards_players_lost)
            cards.pop(0)
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

    
    print("Welcome to Coup developed by Renzo Bedini and Cristobal Moore") 
    num_players = int(input("How many players are going to play?: "))
    deck = ['Duke','Assasin','Captain','Ambassador','Contessa']*3
    random.shuffle(deck)
    players=Player.create_players(deck,num_players)
    #print(deck)
    players_alive = num_players
    log_turn=[]
    print("\nBefore the start of the game, everyone should see their cards\n")
    for i in range(num_players):
        print(players[i].name, "these are your cards:")
        print(players[i].cards)
    cards_players_lost = []
    while players_alive>1:
        for i in range(num_players):   
            if len(players[i].cards)>0:
                print("\nCards of players out of the game: ",cards_players_lost)
                print("\nCoins of each player ")
                for (a, _) in enumerate(players):
                    print(f"{a}:{players[a].name} - {players[a].coins}")
                print("\nPlayers alive:",players_alive,"\n")  
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
                        log_turn.append(players[i].name+' gains 1 coin by using Income action')
                    elif move==2:
                        block=Options.block_action(num_players,players,i)
                        if block==-1:
                            players[i].coins+=General.foreign_help()
                            log_turn.append(players[i].name+' gains 2 coins by using Foreign Help action')
                        elif block !=-1:
                            log_turn.append(players[block].name+ " decide to counterattack Foreign Help action used by "+ players[i].name) 
                            decision = input("Do you want to challenge the player that counterattacked you? (YES or NO)")
                            if decision == 'YES':
                                log_turn.append(players[i].name+ " decides to challenge the counterattack action from "+ players[block].name)
                                player_x = player(block+1)
                                if 'Duke' in player_x:
                                    position=player_x.index('Duke')
                                    print(player_x[position])
                                    player_x,deck = new_card(deck,player_x,position)
                                    log_turn.append(players[i].name+' looses a card for challenging the counterattack')
                                    players[i].cards=delete_card(players[i].cards, players[i].name, cards_players_lost)
                                    if len(players[i].cards)==0:
                                        log_turn.append(players[i].name+" has no more cards")  
                                        log_turn.append(players[i].name+ " is out of the game")   
                                        players_alive = players_alive - 1       
                                else:
                                    log_turn.append(players[block].name+ " looses a card for lying about having it")
                                    player_x=delete_card(player_x, players[block].name, cards_players_lost)
                                    if len(player_x)==0:  
                                        log_turn.append(players[block].name+ " has no more cards") 
                                        log_turn.append(players[block].name+ " is out of the game")
                                        players_alive = players_alive - 1  
                            else:
                                log_turn.append(players[block].name+" blocks Foreign Help action used by "+players[i].name)
                    elif move==3:
                        if players[i].coins>=7:
                            players[i].coins-=7
                            strike=Options.strike_action(num_players, players, players[i].name)
                            log_turn.append(players[i].name+ " chooses to hit "+players[strike].name)
                            log_turn.append(players[strike].name+ " lost a card because he got hit by "+players[i].name)
                            if len(players[strike].cards)==2:
                                General.player_strike(players[strike].cards, players[strike].name, cards_players_lost)
                            else:
                                visible_name = cards_players_lost.index(players[strike].name)
                                cards_players_lost.insert(visible_name+1, players[strike].cards[0])
                                players[strike].cards.pop(0)
                                log_turn.append(players[strike].name+ " has no more cards")
                                log_turn.append(players[strike].name+ " is out of the game")
                                players_alive = players_alive - 1 
                        else:
                            print(players[i].name," doesn't have enough coins to make this action")
                elif choose_1 == 'C':
                    move=Options.menu_character_action()
                    if move==1:
                        challenger=Options.challenge_action(num_players, players, i)
                        if challenger==-1:
                            players[i].coins+=Character.tax()
                            log_turn.append(players[i].name+" gains 3 coins by using Tax action")
                        elif challenger!=-1:
                            log_turn.append(players[challenger].name+ " decide to challenge the Tax action used by "+ players[i].name)
                            if 'Duke' in players[i].cards:
                                position=players[i].cards.index('Duke')
                                print(players[i].cards[position])
                                players[i].cards,deck = new_card(deck,players[i].cards,position)
                                player_x = player(challenger+1)
                                log_turn.append(players[challenger].name+ " looses a card for challenging the action")
                                delete_card(player_x, players[challenger].name, cards_players_lost)
                                if len(players[challenger].cards)==0:  
                                    log_turn.append(players[challenger].name+ " has no more cards")  
                                    log_turn.append(players[challenger].name+ " is out of the game")
                                    players_alive = players_alive - 1  
                                players[i].coins+=Character.tax()
                                log_turn.append(players[i].name+" gains 3 coins by using Tax action")
                            else:
                                delete_card(players[i].cards, players[i].name, cards_players_lost)
                                log_turn.append(players[i].name+ " looses a card for lying about having the card")
                                if len(players[i].cards)==0:  
                                    log_turn.append(players[challenger].name+ " has no more cards")  
                                    log_turn.append(players[challenger].name+ " is out of the game")
                                    players_alive = players_alive - 1  
                            
                    elif move==2:
                        if players[i].coins>=3:
                            players[i].coins-=3
                            challenger=Options.challenge_action(num_players,players,i)  
                            true=True                
                            if challenger!=-1:
                                log_turn.append(players[challenger].name+ " decide to challenge Murder action"+ players[i].name)
                                if 'Assasin' in players[i].cards:
                                    position=players[i].cards.index('Assasin')
                                    print(players[i].cards[position])
                                    players[i].cards,deck = new_card(deck,players[i].cards,position)
                                    player_x = player(challenger+1)
                                    log_turn.append(players[challenger].name+ " looses a card for challenging the action")
                                    delete_card(player_x, players[challenger].name, cards_players_lost)
                                    if len(players[challenger].cards)==0:  
                                        log_turn.append(players[challenger].name+ " has no more cards")  
                                        log_turn.append(players[challenger].name+ " is out of the game")
                                        players_alive = players_alive - 1  
                                else:
                                    log_turn.append(players[i].name+ " looses a card for lying about having the card")
                                    delete_card(players[i].cards, players[i].name, cards_players_lost)
                                    if len(players[i].cards)==0:  
                                        log_turn.append(players[i].name+ " has no more cards")  
                                        log_turn.append(players[i].name+ " is out of the game")
                                        players_alive = players_alive - 1
                                    true=False
                            while true: 
                                true=False                                                                        
                                strike=Options.strike_action(num_players,players, players[i].name)
                                print(players[strike].name, "do you want to counterattack the player that wants to kill you? (YES or NO)")
                                decision = input()
                                if decision == 'YES':
                                    log_turn.append(players[strike].name+ " decides to counterattack the Murder action used by "+players[i].name)
                                    print(players[i].name, "do you want to challenge the player that counterattacked you? (YES or NO)")
                                    decision2 = input()
                                    if decision2 == 'YES':
                                        log_turn.append(players[i].name+ " decide to challenge the counterattack used by "+players[strike].name)
                                        player_x = player(strike+1)
                                        if 'Contessa' in player_x:
                                            position=player_x.index('Contessa')
                                            print(player_x[position])
                                            log_turn.append(players[strike].name+ " has the card to counterattack")
                                            player_x,deck = new_card(deck,player_x,position)
                                            log_turn.append(players[i].name+ " looses a card for challenging the counterattack")
                                            delete_card(players[i].cards, players[i].name, cards_players_lost)
                                            if len(players[i].cards)==0:  
                                                log_turn.append(players[i].name+ " has no more cards")  
                                                log_turn.append(players[i].name+ " is out of the game")
                                                players_alive = players_alive - 1  
                                        else:
                                            log_turn.append(players[strike].name+" doesn't have the card to counterattack")
                                            if len(players[strike].cards)==2:
                                                cards_players_lost.append(players[strike].name)
                                                cards_players_lost.append(players[strike].cards[0])
                                                cards_players_lost.append(players[strike].cards[1])
                                                players[strike].cards.pop(0)
                                                players[strike].cards.pop(0)
                                                log_turn.append(players[i].name+ " assasinated "+players[strike].name)
                                                log_turn.append(players[strike].name+ " has no more cards")
                                                log_turn.append(players[strike].name+ " is out of the game")
                                                players_alive = players_alive - 1  
                                            else:
                                                visible_name = cards_players_lost.index(players[strike].name)
                                                cards_players_lost.insert(visible_name+1, players[strike].cards[0])
                                                players[strike].cards.pop(0)
                                                log_turn.append(players[i].name+ " assasinated "+players[strike].name)
                                                log_turn.append(players[strike].name+ " has no more cards")
                                                log_turn.append(players[strike].name+ " is out of the game")
                                                players_alive = players_alive - 1 
                                    else:
                                        log_turn.append(players[strike].name+ " counterattack the Murder action used by "+players[i].name)

                                else:
                                    player_x = player(strike+1)
                                    Character.murder(player_x, players[strike].name, cards_players_lost)
                                    log_turn.append(players[i].name+ " assasinated "+players[strike].name)
                                    if len(players[strike].cards)==0: 
                                        log_turn.append(players[strike].name+ " has no more cards") 
                                        log_turn.append(players[strike].name+ " is out of the game")
                                        players_alive = players_alive - 1  
            
                    if move==3:
                        challenger=Options.challenge_action(num_players, players, i)   
                        true=True  
                        if challenger!=-1:
                            log_turn.append(players[challenger].name+ " decide to challenge the Extortion action "+ players[i].name)
                            if 'Captain' in players[i].cards:
                                position=players[i].cards.index('Captain')
                                print(players[i].cards[position])
                                players[i].cards,deck = new_card(deck,players[i].cards,position)
                                player_x = player(challenger+1)
                                log_turn.append(players[challenger].name+ " looses a card for challenging the Extortion action")
                                delete_card(player_x, players[challenger].name, cards_players_lost)
                                if len(players[challenger].cards)==0:  
                                        log_turn.append(players[challenger].name+ " has no more cards")
                                        log_turn.append(players[challenger].name+ " is out of the game")
                                        players_alive = players_alive - 1  
                                        
                            else:
                                log_turn.append(players[i].name+ " looses a card for lying about having the card")
                                delete_card(players[i].cards, players[i].name, cards_players_lost)
                                true=False
                                if len(players[i].cards)==0:  
                                    log_turn.append(players[i].name+ " has no more cards")
                                    log_turn.append(players[i].name+ " is out of the game")
                                    players_alive = players_alive - 1
                        while true:
                            true=False
                            steal = Options.stealing_action(num_players, players, players[i].name)
                            log_turn.append(players[i].name+ " decides to Extortion from "+ players[steal].name)
                            print(players[steal].name, " do you want to counterattack the player that wants to Extortion from you? (YES or NO) ")
                            decision = input()
                            if decision == 'YES':
                                log_turn.append(players[steal].name+ " decide to counterattack "+ players[i].name)
                                print(players[i].name, " do you want to challenge the player that counterattacked you? (YES or NO)")
                                decision2 = input()
                                if decision2 == 'YES':
                                    log_turn.append(players[i].name+ " decide to challenge the counterattack "+ players[steal].name)
                                    player_x = player(steal+1)
                                    if 'Ambassador' in player_x:
                                        position=player_x.index('Ambassador')
                                        print(player_x[position])                                    
                                        log_turn.append(players[steal].name+ " has the card to counterattack")
                                        player_x,deck = new_card(deck,player_x,position)
                                        log_turn.append(players[i].name+ " looses a card for challenging the counterattack")
                                        delete_card(players[i].cards, players[i].name, cards_players_lost)
                                        if len(players[i].cards)==0:  
                                            log_turn.append(players[i].name+ " has no more cards")  
                                            log_turn.append(players[i].name+ " is out of the game")
                                            players_alive = players_alive - 1  

                                    elif 'Captain' in player_x:
                                        position=player_x.index('Captain')
                                        print(player_x[position])
                                        log_turn.append(players[steal].name+ " has the card to counterattack")
                                        player_x,deck = new_card(deck,player_x,position)
                                        log_turn.append(players[i].name+ " looses a card for challenging the counterattack")
                                        delete_card(players[i].cards, players[i].name, cards_players_lost)
                                        if len(players[i].cards)==0:  
                                            log_turn.append(players[i].name+ " has no more cards")  
                                            log_turn.append(players[i].name+ " is out of the game")
                                            players_alive = players_alive - 1  
                                    else:
                                        log_turn.append(players[steal].name+ " looses a card for lying about having the card")
                                        player_x = delete_card(player_x, players[steal].name, cards_players_lost)
                                        if len(players[steal].cards)==0:  
                                            log_turn.append(players[steal].name+ " has no more cards")  
                                            log_turn.append(players[steal].name+ " is out of the game")
                                            players_alive = players_alive - 1  
                                        players[i].coins,players[steal].coins = Character.steal(players[i].coins,players[steal].coins)
                                        log_turn.append(players[i].name+ " Extortion coins from "+players[steal].name)
                                else:
                                    log_turn.append(players[steal].name+ " counterattack Extortion action from "+ players[i].name)
                            else:
                                players[i].coins,players[steal].coins = Character.steal(players[i].coins,players[steal].coins)
                                log_turn.append(players[i].name+ " Extortion coins from "+ players[steal].name)
                    if move==4:
                        challenger=Options.challenge_action(num_players, players, i)     
                        if challenger!=-1:
                            log_turn.append(players[challenger].name+ " decide to challenge Exchange action used by"+ players[i].name)
                            if 'Ambassador' in players[i].cards:
                                position=players[i].cards.index('Ambassador')
                                print(players[i].cards[position])
                                players[i].cards,deck = new_card(deck,players[i].cards,position)
                                player_x = player(challenger+1)
                                log_turn.append(players[challenger].name+ " looses a card for challenging Exchange action")
                                delete_card(player_x, players[challenger].name, cards_players_lost)
                                if len(players[challenger].cards)==0:  
                                    log_turn.append(players[challenger].name+ " has no more cards")  
                                    log_turn.append(players[challenger].name+ " is out of the game")
                                    players_alive = players_alive - 1  
                                else:
                                    players[i].cards,deck = Character.swap_cards(players[i].cards,deck)
                                    log_turn.append(players[i].name+ " swaped two cards from the deck")
                            else:
                                log_turn.append(players[i].name+ " looses a card for lying about having the card")
                                delete_card(players[i].cards, players[i].name, cards_players_lost)
                                if len(players[i].cards)==0:  
                                    log_turn.append(players[i].name+ " has no more cards")  
                                    log_turn.append(players[i].name+ " is out of the game")
                                    players_alive = players_alive - 1  
                        else:
                            players[i].cards,deck = Character.swap_cards(players[i].cards,deck)
                            log_turn.append(players[i].name+ " swaped two cards from the deck")
                for a in log_turn:
                    print("\n ->",a)
                if players_alive==1:
                    break
                
    for i in range(num_players):    
            if len(players[i].cards)>0:  
                print(players[i].name, "is the winner! Congratulations!")
                print("??Hope you liked the game!")                

if __name__ == "__main__":
    main()