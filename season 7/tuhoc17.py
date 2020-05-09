from random import *

count = 0

while True:
    a = randint(0,100)
    b = randint(0,100)
    c = randint(0,1)

    if c == 0:
        print(a,"+",b,"=")
        d = randint(0,1)

        if d == 0:
            print(a+b)
            x = input("True or False? ")
            if x == "T" or x == "t":
                print("True answer, let's continue")
                count = count + 1
                print("your score is ", count)
            if x == "F" or x == "f":
                print("False, game over!")
                break
        
        if d == 1:
            print(randint(a+b-3,a+b+3))
            y = input("True or False? ")
            if y == "T" or y == "t":
                print("False, game over!")
                break
            if y == "F" or y == "f":
                print("True answer, let's continue")
                count = count + 1
                print("your score is ", count)

    if c == 1:
        print(a,"-",b,"=")
        e = randint(0,1)

        if e == 0:
            print(a-b)
            z = input("T or F")
            if z == "T" or z == "t":
                print("True answer, let's continue")
                count = count + 1
                print("your score is ", count)
            if z == "F" or z == "f":
                print("False, game over!")
                break 

        if e == 1:
            print(randint(a-b-3,a-b+3))
            q = input("T or F")
            if q == "T" or q == "t":
                print("False, game over!")
                break
            if q == "F" or q == "f":
                print("True answer, let's continue")
                count = count + 1
                print("your score is ", count)

