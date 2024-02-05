from dataclasses import dataclass

@dataclass
class Cheese():
    type: str
    age: int #months
    texture: str


    def printInfo(self) -> None:
        print('type:', self.type)
        print('age:', self.age, 'months')
        print('texture:', self.texture)

def main():
    cheese1 = Cheese('cheddar', 3, 'firm')
    cheese2 = Cheese('swiss', 10, 'hard')
    cheese3 = Cheese('colby', 1, 'semi-hard')

    print('CHEESE ONE -')
    cheese1.printInfo()
    print('CHEESE TWO -')
    cheese2.printInfo()
    print('CHEESE THREE -')
    cheese3.printInfo()

if __name__ == "__main__":
    main()



