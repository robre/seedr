#!/usr/bin/python3
#-*- coding: utf-8 -*-
# 
# note:
# s/random/pseudo-random
# VISUAL lines can be removed, they are just used to print the method 
enc = "utf-8"

import random
import time
import hashlib
hash_methods = list(hashlib.algorithms_guaranteed) # more stable then algorithms_available

method = "" # VISUAL

def getRandomMethod(): 
    return hashlib.new(random.choice(hash_methods))

#######################

def stringShuffle(s):
    return ''.join(random.sample(s,len(s)))

def randHash(s): # hash a string with a random hashing function
    m = getRandomMethod()
    m.update(bytes(s,enc))
    return m.hexdigest()

def addTime(s):
    return s + str(time.time())

def addRand(s):
    return s + str(random.random())

#######################
# You can add more functions above, to increase entropy. 
# They just need to take one string argument and return a string.
# You will also need to add the function name to the functions list below.
#######################

def factory(r):
    global method               # VISUAL
    if r == 'init':
        method += 'time.time()' # VISUAL
        r = str(time.time())
    functions = ['stringShuffle', 'randHash', 'addTime', 'addRand', '']
    f = random.choice(functions)
    if f == '':
        return r
    else:
        method = f + '(' + method + ')' # VISUAL
        return factory(eval(f + '(r)')) 

def main():
    global method                   # VISUAL
    try:
        while True:

           # print(getRandomMethod().name)
            print("\n\n")
            print(factory('init'))
            print("method used:")
            print(method)                   # VISUAL
            method = ""                     # VISUAL
            #random.seed(factory('init'))
    except KeyboardInterrupt:
        return 0



if __name__ == "__main__":
    main()

