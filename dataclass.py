from dataclasses import dataclass

@dataclass
class Cheese():
    type: str
    age: int #months
    texture: str

def main():
    cheese1 = Cheese('cheddar', 3, 'firm')
    cheese2 = Cheese('swiss', 10, 'hard')
    cheese3 = Cheese('colby', 1, 'semi-hard')

    print('CHEESE ONE -')
    print('type:', cheese1.type)
    print('age:', cheese1.age, 'months')
    print('texture:', cheese1.texture)
    print('CHEESE TWO -')
    print('type:', cheese2.type)
    print('age:', cheese2.age, 'months')
    print('texture:', cheese2.texture)
    print('CHEESE THREE -')
    print('type:', cheese3.type)
    print('age:', cheese3.age, 'months')
    print('texture:', cheese3.texture)

if __name__ == "__main__":
    main()



