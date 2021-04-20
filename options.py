class Options:
    
    def __init__(self,num_players):
        self.__num_players=num_players
    
    def menu_character_action(self):
        print ("Choose one of the next options")
        print("1: Duke (TAX)") 
        print("2: Assasin (MURDER)")  
        print("3: Captain (BLACKMAIL)")
        print("4: Ambassador (SWITCH)")
        return(int(input()))

    def menu_general_action(self):
        print ("Choose one of the next options")
        print("1: Take_coin") 
        print("2:Foreign_Help")  
        print("3: Strike")
        return(int(input()))

    def block_action(num_players):
        print ("Who wants to block? ")
        print("0: No One block")
        print("1: Player 1 blocks") 
        print("2: Player 2 blocks")  
        print("3: Player 3 blocks")
        if num_players == 4:
            print("4: Player 4 block")
        return(int(input()))
    
    def strike_action(num_players):
        print ("Which player do you want to hit?")
        print ("1: Player 1")
        print("2: Player 2")  
        print("3: Player 3")
        if num_players == 4:
            print("4: Player 4")
        return(int(input()))
    
    def challenge_action(num_players):
        print ("Who wants to challenge? ")
        print("0: No One challenge")
        print("1: Player 1 challenges") 
        print("2:Player 2 challenges")  
        print("3: Player 3 challenges")
        if num_players == 4:
            print("4: Player 4 challenges")
        return(int(input()))

    def stealing_action(num_players):
        print ("Which player do you want to steal from?")
        print ("1: Player 1")
        print("2: Player 2")  
        print("3: Player 3")
        if num_players == 4:
            print("4: Player 4")
        return(int(input()))