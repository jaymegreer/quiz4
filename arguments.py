import argparse


def parse() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help = "Enter a string", dest = "input_string", type = str)
    parser.add_argument(help = "Enter an integer", dest = "input_int", type = int)
    parser.add_argument(help = "Enter a float", dest = "input_float", type = float)
    
    args = parser.parse_args()

    inputStr = args.input_string
    inputInt = args.input_int
    inputFloat = args.input_float

    print('string:', inputStr)
    print('int:', inputInt)
    print('float:', inputFloat)

if __name__=='__main__': 	
    parse()