#!/usr/bin/python3
#-*- coding: utf-8 -*-
# 
enc = "utf-8"

import random
import time
import hashlib
hash_methods = list(hashlib.algorithms_guaranteed) # more stable then algorithms_available

method = ""

def getRandomMethod():
    return hashlib.new(random.choice(hash_methods))

#######################

def stringShuffle(s):
    return ''.join(random.sample(s,len(s)))

def randHash(s):
    m = getRandomMethod()
    m.update(bytes(s,enc))
    return m.hexdigest()

def addTime(s):
    return s + str(time.time())

def addRand(s):
    return s + str(random.random())

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
    try:
        while True:

           # print(getRandomMethod().name)
            global method                   # VISUAL
            print("\n\n")
            print(factory('init'))
            print("method used:")
            print(method)                   # VISUAL
            method = ""                     # VISUAL
            #random.seed(factory())
    except KeyboardInterrupt:
        return 0



if __name__ == "__main__":
    main()

