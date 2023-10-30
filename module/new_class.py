class Drink:
    
    _volume = 200
    
    def __init__(self, name, price):
        self.name = name 
        self.price = price
        self._remains = self._volume
    
    def drink_info(self):
        print (f'Named: "{self.name}". Price: {self.price} EUR. volume: {self._volume} ml. Remains: {self._remains} ml.')
    
    def _is_enough(self, need):
        if self._remains >= need and self._remains > 0:
            return True
        print ('Not enough drink left')
        return False
    
    def sip(self):
        if self._is_enough(20) == True:
            self._remains -= 20
            print ('Take a sip')
            
    def small_sip(self):
        if self._is_enough(10) == True:
            self._remains -= 10
            print ('Take a small sip')
    
    def drink_all(self):
        if self._is_enough(0) == True:
            self._remains = 0
            print ('Drink a drink in one gulp')
    
    # say the cost of a drink
    def tell_price(self):
        print (f'cost of my drink {self.price} EUR')
        
        
        
class Juice(Drink):

    _juice_name = 'juice'    

    def __init__(self, price, taste):
        super().__init__ (self._juice_name, price)
        self.taste = taste

    def drink_info(self):
        print (f'Taste: {self.taste}. Price: {self.price} EUR. volume: {self._volume} ml. Remains: {self._remains} ml.')