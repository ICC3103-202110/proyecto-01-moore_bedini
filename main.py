import random

print("Welcome to Coup developed by Renzo bedini and Cristobal Moore")
num_players = int(input("Indique la cantidad de jugadores que van a jugar: "))

def main():

    D = 'Duque'
    A = 'Asesino'
    C = 'Capitan'
    E = 'Embajador'
    CO = 'Condesa'
    deck = [D,A,C,E,CO]*3
    random.shuffle(deck)
    
    Cards_P1 = [ deck[0],deck[1] ]
    print(Cards_P1)
    Cards_P2 = [ deck[2],deck[3] ]
    print(Cards_P2)
    Cards_P3 = [ deck[4],deck[5] ]
    print(Cards_P3)
    if num_players == 4:
        Cards_P4 = [ deck[6],deck[7] ]
        print(Cards_P4)
    

    

if __name__ == "__main__":
    main()