import sys
import time
import random

MIN_NUMBER = 5e-324
FUNNY_NUMBER = random.choice([69, 42, 420, 25.8069758011, 96, 288, 77])
MAX_SPEED = 299_792_458

class TypeMaybe:
    def __init__(self) -> None:
        pass

    def __call__(self) -> bool:
        return random.choice([true, false])
    
class InvalidStringError(Exception):
    def __init__(self, msg: str = "String is invalid.") -> None:
        super().__init__(msg)

class Error420(Exception):
    def __init__(self, msg: str = "You too high to operate.") -> None:
        super().__init__(msg)

class UDumbError(Exception):
    def __init__(self, msg: str = "U just ain't built for this.") -> None:
        super().__init__(msg)

class Queue:
    def __init__(self, queue: list = []) -> None:
        self.queue: list = queue

    def pop(self, i: int):
        return self.queue.pop(i)
    
    def replace(self, i: int, newVal: any):
        self.queue[i] = newVal

    def next(self):
        self.queue.pop(0)

        for i in range(len(self.queue)):
            print(i)
        
true, false, maybe = True, False, TypeMaybe()

def println(line: any) -> None:
    '''
    Outputs a line in the console that the program is running inside.
    If the user enters a string literal with multiple lines the program will
    throw an InvalidStringError.
    '''

    if "\n" in str(line): 
        raise InvalidStringError("Newlines are not allowed in println function.")
    
    else:
        sys.stdout.write(f"{line}\n")
        return

def part(num: float | int) -> float | int:
    '''
    Returns the partial value of a number.
    The partial value of a number is always negative.
    '''

    return -abs(num)

def jsAdd(num1: str | float | int, num2: str | float | int) -> str | float | int:
    '''
    Returns the sum of two numbers according to Javascript.
    Can be problematic in large codebases.
    '''
    
    if type(num1) in [int, float] and type(num2) in [int, float]:
        return num1 + num2
    
    elif type(num1) == str or type(num2) == str:
        return str(num1) + str(num2)

def jsSub(num1: str | float | int, num2: str | float | int) -> str | float | int:
    '''
    Returns the difference of two numbers according to Javascript.
    Can be problematic in large codebases.
    '''

    if type(num1) in [int, float] and type(num2) in [int, float]:
        return num1 - num2
    
    elif type(num1) == str or type(num2) == str:
        res = float(num1) - float(num2)

        if res.is_integer():
            return int(res)

        else:
            return res
    
def isTrulyEven(num: int, limit: int = 999999) -> bool:
    '''
    Returns a boolean based on whether a number is even or not.
    If iterations exceed the limit the program will return the 
    maybe boolean.
    '''

    i = 0

    while num != 1:
        num = num / 2

        if i == limit: 
            return maybe()

        else:
            i += 1 
            continue

    return true

def procrastinate(t) -> None:
    '''
    Stops the execution of the program for a set time in seconds
    so you can procrastinate while the code runs. Is just an 
    extension of time.sleep().
    '''

    if type(t) not in [float, int]:
        raise TypeError("Argument 't' is not a float or int.")
    
    else:
        println(f"Procrastinating for {t}s...")
        time.sleep(t)

        return

def basicAhh():
    '''
    Does what every basic ahh starter program does.
    **Hint, it prints Hello world!**
    '''

    println("Hello World!")