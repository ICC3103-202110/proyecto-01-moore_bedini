class Player:
    def __init__ (self, coins):
        self.__coins=coins
        
    @property
    def coins(self):
        return self.__coins
    
    @coins.setter
    def coins(self, value):
        self.__coins= value
        



