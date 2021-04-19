from general_action import General
import random
def main():
    def menu_general_action():
        print ("Choose one of the next options")
        print("1: Take_coin") 
        print("2:Foreign_Help")  
        print("3: Strike")
        return(int(input()))

    def block_action(num_players):
        print ("Who wants to block? ")
        print("0: No One block")
        print("1: Player 1 block") 
        print("2:Player 2 block")  
        print("3: Player 3 block")
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
        
    maze= deck[-(15-(num_players)*2):]
    print(maze)
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
                    hit=strike_action(num_players)
                    if hit==2:
                        General.player_hit(Cards_P2)
                    if hit==3:
                            General.player_hit(Cards_P3)
                    if hit==4:
                            General.player_hit(Cards_P4)
                    Money_P1= Money_P1-7
                    

if __name__ == "__main__":
    main()