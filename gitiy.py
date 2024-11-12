import random
import time
import math
import decimal
import cmath
import os
import sys
import threading
import numpy
import manim
import re
import typing
import rich
import string
import faker
import transformers
import keras
import tensorflow
import mpmath
import matplotlib
import datetime
import requests
import discord
import discord.ext
import json
import http
import socket
import socketserver
import tkinter
import ursina
import pygame
import subprocess
import turtle
import turtledemo
import csv
import __future__
null = None
nullnum = 0.0 + 0.0j
nullstr = ""
nullbool = False
nulllist = []
nulltuple = ()
nulldict = {}
char_groups = {
    "russian": "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    "english": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "empty": "",
    "numbers": "0123456789",
    "symbols": "!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~",
    "finance": "$£€¢₽₹¥₱₿",
    "math": "+-*/=<>≠≤≥",
    "science": "∞∑∏∫≡≠≈",
    "programmer": "<>{}[]()#@&|\\"
}
def shift(null):
    return chr((ord(null) - ord('a') + 3) % 26 + ord('a'))
def nullCheck(*null: typing.Any) -> bool:
    return null == nullnum or null == nullstr or null == nullbool or null == nulllist or null == nulltuple or null == nulldict
def random_str(k: str) -> str:
    k = input()
    ''.join(random.choice(string.ascii_letters + string.digits), k)
def random_str_char_groups(k: int) -> str:
    char_group = random.choice(list(char_groups.keys()))
    return ''.join(random.choice(char_groups[char_group]) for _ in range(k))
def corrector(string, width, symbol):
    padding = symbol * width
    return padding + string + padding
def cryptCeasar(message, shift=2):
    cipher_text = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            cipher_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            cipher_text += char
def ai_generate(*prompt, temp=0.3):
    model_name = "gpt2"
    tokenizer = transformers.GPT2Tokenizer.from_pretrained(model_name)
    model = transformers.GPT2LMHeadModel.from_pretrained(model_name)
    inputs = tokenizer.encode(prompt[0], return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, temperature=temp, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
class config:
    @staticmethod
    def get_config(key: str) -> str:
        with open('config.json', 'r') as file:
            config = json.load(file)
        return config.get(key, "")
    @staticmethod
    def set_config(key: str, value: str) -> None:
        with open('config.json', 'r') as file:
            config = json.load(file)
        config[key] = value
        with open('config.json', 'w') as file:
            json.dump(config, file)
            print(f'Конфигурация изменена: {key} -> {value}')
            print('Сохранено')
    @staticmethod
    def add_to_config(key: str, value: str) -> None:
        with open('config.json', 'r') as file:
            config = json.load(file)
        config.setdefault(key, []).append(value)
        with open('config.json', 'w') as file:
            json.dump(config, file)
            print(f'Добавлено значение {value} к ключу {key}')
            print('Сохранено')
class io:
    @staticmethod
    def read(filename: str) -> str:
        with open(filename, 'r') as file:
            return file.read()
        return ""
    @staticmethod
    def write(filename: str, data: str) -> None:
        with open(filename, 'w') as file:
            file.write(data)
    @staticmethod
    def append(filename: str, data: str) -> None:
        with open(filename, 'a') as file:
            file.write(data)
    @staticmethod
    def delete(filename: str) -> None:
        os.remove(filename)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    @staticmethod
    def exists(filename: str) -> bool:
        return os.path.exists(filename)
class human:
    def __init__(self, name, age, education, skills):
        self.name = name
        self.age = age
        self.education = education
        self.skills = skills
        self.is_criminal = False
    def make_criminal(self):
        self.is_criminal = True
        print(f'{self.name} стал преступником!')
        self.education = 'Уголовное дело'
        self.skills = ['Убийство', 'Бандитизм', 'Ограбление']
class mathbox:
    pi = 3.141592653589793
    e = 2.718281828459045
    golderratio = 1.618033988749894
    strange0304 = 0.30000000000000004
    inf = numpy.inf
    neginf = -( numpy.inf )
    nan = numpy.nan
    def is_nan(n):
        if n+1==n:
            return numpy.nan_to_num(n)
        else:
            return n
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
    def recurcive(i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            return mathbox.recurcive(i-1) + mathbox.recurcive(i-2)
    def fractal(i, n, c, z):
        if i == 0:
            return c
        else:
            return mathbox.fractal(i-1, n, c, z * z + c)
    def numFloatPointMath():
        return decimal.Decimal(1) / decimal.Decimal(0.3) * (decimal.Decimal(2) ** decimal.Decimal(1000000))
class theoryofeverything:
    def euler_phi_function(n):
        phi = n
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if i * i == n:
                    phi -= phi // i
                else:
                    phi -= (phi // i) + (phi // (n // i))
        return phi
    def euler_totient_function(n):
        phi = n
        for i in range(2, n+1):
            if theoryofeverything.is_prime(i):
                phi -= phi // i
    plank = 6.67430e-11
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
    
    def __truediv__(self, other):
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
    mcmusic = 0xC418
    bbmusic = 0xCA98
    def __init__(self):
        pass
    def pop(self):
        rich.print("Popping from funbox...")
        time.sleep(0.5)
        print("Pop!")
        return random.randint(1, 100)
    def float_swim():
        print(f"{float} далеко уплыл!")
        raise ExceptionGroup(f"{float}")
    nullcontents = []
    partyGroup = []
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
    def robingoodchoice():
        sleep_print("Хочешь ада?")
        anwser = input("(y/n): ")
        if not anwser.find("y") != -1:
            while True:
                print("A", end="")
        elif not anwser.find("n") != -1:
            print("Ок, не буду)")
        else:
            print("????")
    def tracebackTroll():
        for i in range(100):
                print("ХA", end="")
                print("\n")
        raise WindowsError(" АХАХАХА! С ПЕРВЫМ АПРЕЛЯ ПЕДРИЛА!")
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
class turtle_demos:
    scr = turtle.Screen()
    joe = turtle.Turtle()
    def __init__(self):
        self.turtles = [self.joe]
    def draw_square(self, length=90):
        for _ in range(4):
            self.joe.forward(length)
            self.joe.right(90)
    def chaos():
        for _ in range(10):
            turtle_demos.joe.forward(random.randint(10, 200))
            turtle_demos.joe.right(random.randint(0, 360))
            turtle_demos.joe.color(random.choice(["red", "green", "blue", "yellow", "lightblue", "pink"]))
    def draw_circle(self, radius=90):
        self.joe.circle(radius)
class gitiybox:
    chats = {"main": []}
    partyGroup = {}
    def __init__(self):
        self.gitiybox = []
    def chats():
        while True:
            chat = input("New chat: ")
            if chat:
                gitiybox.gitiybox.append(chat)
                print(f"Chat '{chat}' added to gitiybox.")
            else:
                print("Chat name can't be empty.")
                break
    def chat(chat, party, action="enter"):
        if chat in gitiybox:
            print(f"{action} chat '{chat}' to party.")
            party.partyGroup.append(chat)
            while True:
                message = input(f"{chat}: ")
                if message:
                    print(f"{chat}: {message}")
                else:
                    print("Message can't be empty.")
                    break
                requests.post(message)
                requests.get()
        else:
            print(f"Chat '{chat}' not found in gitiybox.")
    def remove(chat, party):
        if chat in party.partyGroup:
            print(f"Removing chat '{chat}' from party.")
            party.partyGroup.remove(chat)
        else:
            print(f"Chat '{chat}' not found in party.")
    def clear(party):
        print("Clearing gitiybox...")
    def chat_history(chat):
        if chat in gitiybox:
            print(f"Chat history for chat '{chat}':")
            for message in gitiybox[chat]:
                print(message)
        else:
            print(f"Chat '{chat}' not found in gitiybox.")
    def nullcontents(self):
        return rich.print("Gitiybox is empty.")
    def __len__(self):
        return len(self.gitiybox)
    def __getitem__(self, key):
        return self.gitiybox[key]
    def __setitem__(self, key, value):
        self.gitiybox[key] = value
        print(f"Chat '{key}' updated.")
    def __delitem__(self, key):
        del self.gitiybox[key]
        print(f"Chat '{key}' removed from gitiybox.")
    def __iter__(self):
        return iter(self.gitiybox)
    def __reversed__(self):
        return reversed(self.gitiybox)
    def __contains__(self, item):
        return item in self.gitiybox
class nullbox:
    def __init__(self):
        self.nullbox = []
        self.nullcontents()
    def checkNullContents(null, content):
        if content:
            null.nullbox.append(content)
            print(f"Content '{content}' added to nullbox.")
        else:
            print("Content can't be empty.")
            return None
    altNullContents = [0]
    def checkRelateToNull(null, obj):
        if obj in null.nullbox:
            print(f"Object '{obj}' related to nullbox.")
        else:
            print(f"Object '{obj}' not related to nullbox.")
