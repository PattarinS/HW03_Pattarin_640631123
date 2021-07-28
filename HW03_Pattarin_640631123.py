# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:58:52 2021

@author: User
"""

N = int(input("How many (N) in the pile:"))
print("there are {} sticks in the pile.".format(N))
name = input("What is your name:")
x = 1

if N%3 == 0 or N%3 == 2:
    print("Computer go first.\n")
        
else:
    print("You go first.\n")
    
if N%3 == 0 or N%3 == 2:
    while N > 0:
        if x==1 and N%3 == 0:
            com = 2
            print("I,smart computer,takes :", com)
            N = N - com
            print("there are {} sticks in the pile.\n".format(N))
            x= x+1   
        elif x==1 and N%3 == 2:
            com = 1
            print("I,smart computer,takes :", com)
            N = N - com
            print("there are {} sticks in the pile.\n".format(N))
            x= x+1
            
        i = int(input("{},how many sticks you will take (1 or 2):".format(name)))
        while i < 1 or i > 3:
            print("No,you cannot take less than 1 and more than 2 sticks!")
            i = int(input("{},how many sticks you will take (1 or 2):".format(name)))
        N = N - i
        print("there are {} sticks in the pile.\n".format(N))
            
        if i == 1:
            com = 2
            print("I,smart computer,takes :", com)
            N = N - com
            print("there are {} sticks in the pile.\n".format(N))
        elif N > 0 :
            com = 1
            print("I,smart computer,takes :", com)
            N = N - com
            print("there are {} sticks in the pile.\n".format(N))
                
        if N <= 0:
            print(name, ",takes the last stick.\n")
            print("I,smart computer, win  !!!!")
                
else:
    while N > 0:
        i = int(input("{},how many sticks you will take (1 or 2):".format(name)))
        while i < 1 or i > 3:
            print("No,you cannot take less than 1 and more than 2 sticks!")
            i = int(input("{},how many sticks you will take (1 or 2):".format(name)))
    
        N = N - i
        print("there are {} sticks in the pile.\n".format(N))
    
        if N == 0:
            print(name, ",takes the last stick.\n")
            print("I,smart computer, win  !!!!")
        else :
            if i == 1:
                com = 2
                print("I,smart computer,takes :", com)
                N = N - com
                print("there are {} sticks in the pile.\n".format(N))
            else:
                com = 1
                print("I,smart computer,takes :", com)
                N = N - com
                print("there are {} sticks in the pile.\n".format(N))
            if N < 1:
                print("I,smart computer,takes the last stick.\n")
                print(name, "win ( I, smart computer, am sad T_T) ")                
                
                
                
                
                