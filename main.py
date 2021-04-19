from general_action import General
import random
def main():
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

    def block_action(num_players):
        print ("Who wants to block? ")
        print("0: No One block")
        print("1: Player 1 blocks") 
        print("2:Player 2 blocks")  
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
        choose_1= input("Player 1, choose a general (write G) or character accion (write C): ")            
        if choose_1 =='G':
            move=menu_general_action()
            if move==1:
                Money_P1+=General.gain_coin()
                print(Money_P1)
            if move==2:
                block=block_action(num_players)
                if block==0:
                    Money_P1+=General.foreign_help()
                    print(Money_P1)
            if move==3:
                if Money_P1>=7:
                    strike=strike_action(num_players)
                    if strike==2:
                        General.player_strike(Cards_P2)
                    if strike==3:
                            General.player_strike(Cards_P3)
                    if strike==4:
                            General.player_strike(Cards_P4)
                    Money_P1= Money_P1-7
        if choose_1 == 'C':
            move=menu_character_action()
            if move==1:
                challenger=challenge_action(num_players)
                block=block_action(num_players)
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