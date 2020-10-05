import os
from os import system
system("title " + "CoinFlip")

import random

import sys,time

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

heads = """
  _    _                _     
 | |  | |              | |    
 | |__| | ___  __ _  __| |___ 
 |  __  |/ _ \/ _` |/ _` / __|
 | |  | |  __/ (_| | (_| \__ \\
 |_|  |_|\___|\__,_|\__,_|___/
"""
tails = """
 _______    _ _     
 |__   __|  (_) |    
    | | __ _ _| |___ 
    | |/ _` | | / __|
    | | (_| | | \__ \\
    |_|\__,_|_|_|___/
 """

ans = True

while ans:
    close = input("'Close' to exit ").lower()
    cls()
    
    answer = random.randint(1,2)

    if close == "close":
        sys.exit()

    elif answer == 1:
        print(heads)

    elif answer == 2:
        print(tails)
