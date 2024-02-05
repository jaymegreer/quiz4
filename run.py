from mod1 import function1 as one
from mod2 import function2 as two
from mod3 import function3 as three

def run() -> None:
    one.funct1()
    two.funct2()
    three.funct3()

if __name__=="__main__":
    run()
