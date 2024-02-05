from abc import ABC, abstractmethod

class Dance(ABC):
    @abstractmethod
    def movement(self):
        pass

    @abstractmethod
    def trick(self):
        pass

class Ballet(Dance):
    def __init__(self, plie, jete):
        self.plie = plie
        self.jete = jete

    def movement(self):
        return self.plie
    
    def trick(self):
        return self.jete 


class Tap(Dance):
    def __init__(self, shuffle, wing):
        self.shuffle = shuffle
        self.wing = wing

    def movement(self):
        return self.shuffle
    
    def trick(self):
        return self.wing
    
def main():
    balletClass = Ballet(plie="demi", jete="grande")
    print(balletClass.movement(), "plies at the barre")
    print(balletClass.trick(), "jetes across the floor")
    
    tapClass = Tap(shuffle="rolling", wing="double")
    print(tapClass.trick(), "wings at the barre")
    print(tapClass.movement(), "shuffles across the floor")

if __name__ == "__main__":
    main()
