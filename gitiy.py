import random
import time
import math
import cmath
import os
import numpy
import re
import typing
import rich
# not finished
null = None
nullnum = 0.0 + 0.0j
nullstr = ""
nullbool = False
nulllist = []
nulltuple = ()
nulldict = {}
class mathbox:
    pi = 3.141592653589793
    e = 2.718281828459045
    fi = 1.618033988749894
    inf = numpy.inf
    neginf = -( numpy.inf )
    nan = numpy.nan
    def is_integer(n):
        return isinstance(n, int)
    def is_float(n):
        return isinstance(n, float)
    def is_complex(n):
        return isinstance(n, complex)
    def is_zero(n):
        return n == 0.0
    def is_positive(n):
        return n > 0.0
    def is_negative(n):
        return n < 0.0
    def is_even(n):
        return n % 2 == 0
    def is_odd(n):
        return n % 2!= 0
    def is_triangular(n):
        return math.isqrt(n) * (math.isqrt(n) + 1) // 2 == n
    def is_square(n):
        return math.isqrt(n)**2 == n
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_seq = [0, 1]
            for i in range(2, n):
                fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
            return fib_seq
    def gcd(a, b):
        while b!= 0:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return abs(a * b) // mathbox.gcd(abs(a), abs(b))
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * math.factorial(n-1)
    def power(base, exponent):
        return base ** exponent
    def fibonacci_iterative(n):
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq
class surreal:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
    def __add__(self, other):
        if isinstance(other, surreal):
            return surreal(self.real + other.real, self.imaginary + other.imaginary)
        else:
            return surreal(self.real + other, self.imaginary)
    
    def __sub__(self, other):
        if isinstance(other, surreal):
            return surreal(self.real - other.real, self.imaginary - other.imaginary)
        else:
            return surreal(self.real - other, self.imaginary)
    
    def __mul__(self, other):
        if isinstance(other, surreal):
            real = self.real * other.real - self.imaginary * other.imaginary
            imaginary = self.real * other.imaginary + self.imaginary * other.real
            return surreal(real, imaginary)
        else:
            return surreal(self.real * other, self.imaginary * other)
    
    def __div__(self, other):
        if isinstance(other, surreal):
            denominator = other.real**2 + other.imaginary**2
            real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
            return surreal(real, imaginary)
        else:
            return surreal(self.real / other, self.imaginary / other)
def sleep_print(message, duration=0.1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(duration)
    print("\n")
class funbox:
    def __init__(self):
        pass
    def pop(self):
        rich.print("Popping from funbox...")
        time.sleep(0.5)
        print("Pop!")
        return random.randint(1, 100)
    nullcontents = []
    def nullcontents(self):
        return rich.print("Funbox is empty.")
    def push(self, item):
        rich.print(f"Pushing {item} into funbox...")
        time.sleep(0.5)
        print("Push!")
        return item
    def peek(self):
        rich.print("Peeking at funbox...")
        time.sleep(0.5)
        return self.pop()
    def clear(self):
        rich.print("Clearing funbox...")
        time.sleep(0.5)
        self.nullcontents()
        return None
class eater:
    def __init__(self):
        pass
    def eat(self, element):
        rich.print(f"Eating {element}...")
        time.sleep(0.5)
        print("Yum!")
        del element
        return None
    def chaosDelete(self, elements):
        rich.print("Chaos deleting elements...")
        time.sleep(0.5)
        for element in elements:
            self.eat(element)
            del element
        return None
    def nullcontents(self):
        return rich.print("No elements to eat.")
class __class__:
    def __init__(self):
        raise Exception("Cannot instantiate abstract class.")
    def __func__(self, other):
        raise Exception("Cannot call abstract method.")
    def __var__(self):
        var = None
    def __str__(self, string):
        return str(string)
    def __add__(self, other, a, b):
        return a + b
    def __sub__(self, other, a, b):
        return a - b
    def __mul__(self, other, a, b):
        return a * b
    def __truediv__(self, other, a, b):
        return a / b
    def __lt__(self, other, a, b):
        return a < b
    def __le__(self, other, a, b):
        return a <= b
    def __eq__(self, other, a, b):
        return a == b
    def __ne__(self, other, a, b):
        return a != b
