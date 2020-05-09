from random import *        
while True:                
    a = randint(0,100)        
    b = randint(0,100)       
    c = randint(0,1)          
    d = randint(0,2)          
    e = randint(0,2)          
    diem = 0                   


    if c == 0:                                    
        print(a,'+',b,'=')
        if d == 0:
            print(a+b)
            f = input("T or F?")
            if f == 'T' or f == 't':
                diem = diem + 1
            if f == 'F' or f == "f":
                print('sai r')
                break
        
        if d == 1:
            print(a+b+5)
            f = input("T or F?")
            if f == 'F' or f == 'f':
                diem = diem + 1    
            if f == 'T' or f == 't':
                print('sai r')
                break

        if d == 2:
            print(a+b-5)
            f = input("T or F?")
            if f == 'F' or f == 'f':
                diem = diem + 1    
            if f == 'T' or f == 't':
                print('sai r')
                break


    if c == 1:
        print(a,'-',b,'=')
        if e == 0:
            print(a+b)
            f = input("T or F?")
            if f == 'T' or f == 't':
                diem = diem + 1
            if f == 'F' or f == 'f':
                print('sai r')
                break

        if e == 1:
            print(a+b+5)
            f = input("T or F?")
            if f == 'F' or f =='f':
                diem = diem + 1    
            if f == 'T' or f == 't':
                print('sai r')
                break

        if d == 2:
            print(a+b-5)
            f = input("T or F?")
            if f == 'F' or f == 'f':
                diem = diem + 1    
            if f == 'T' or f == 't':
                print('sai r')
                break
                

                



