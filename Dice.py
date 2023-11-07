import numpy as np

class Dice:
    def __init__(self) -> None:
        self.result = []
    
    def roll(self):
        self.result = [np.random.randint(1,7),np.random.randint(1,7)]
        self.is_double()
        return self

    def is_double(self):
        if self.result[0]==self.result[1]:
            if not len(self.result)==4:
                self.result=self.result+self.result
            return True
        return False
        
    
    def __str__(self):
        return str(self.result)