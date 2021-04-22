from players import Player
class Options:
    
    def __init__(self,num_players):
        self.__num_players=num_players
    
    def menu_character_action():
        print ("Choose one of the next options")
        print("1: Duke (TAX)") 
        print("2: Assasin (MURDER)")  
        print("3: Captain (BLACKMAIL)")
        print("4: Ambassador (SWITCH)")
        return(int(input()))

    def menu_general_action():
        print ("Choose one of the next options")
        print("1: Take_coin") 
        print("2:Foreign_Help")  
        print("3: Strike")
        return(int(input()))

    def block_action(num_players, players, i):
        for a in range(num_players):
            if len(players[a].cards)>0:  
                if players[i].name!=players[a].name:
                    print (players[a].name," want to block? YES or NO")
                    b=input()
                    if b=='YES':                
                        return int(a)
        return int(-1)

    def strike_action(num_players, players, name):
        for a in range(num_players):
            if len(players[a].cards)>0:
                if players[a].name!=name:
                    print ("Do you want to hit,", players[a].name," YES or NO")
                    b=input()
                    if b=='YES':                
                        return int(a)

    
    def challenge_action(num_players, players, i):
        for a in range(num_players):
            if len(players[a].cards)>0:  
                if players[i].name!=players[a].name:
                    print (players[a].name," want to challenge? YES or NO")
                    b=input()
                    if b=='YES':                
                        return int(a)
        return int(-1)

    def stealing_action(num_players,players, name):
        for a in range(num_players):
            if len(players[a].cards)>0:
                if players[a].name!=name:
                    print ("Do you want to steal from,", players[a].name," YES or NO")
                    b=input()
                    if b=='YES':                
                        return int(a)