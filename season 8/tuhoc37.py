import random
while True:
    alo = ['cuctacuctac','cuccuccuc','cuctactaccuc']
    random.shuffle(alo)
    alo1 = alo[0]
    a = list(alo1)
    random.shuffle(a)
    print(*a)
    b = input('ban doan xem do la chu gi? ')
    if b == alo1:
        print('ban doan dung roi')
    else:
        print('ban doan sai r')    
