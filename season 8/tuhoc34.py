ilike = ['game','do an','nuoc ngot']
muongi = input('ban muon C hay U hay R hay D? ')
if muongi == 'C' or 'c':
    b = input('ban muon them phan tu nao?')
    ilike.append(b)
    print(ilike)
if muongi == 'R' or 'r':
    if ilike == 0:
        print('ko co phan tu nao')
    for abc in enumerate(ilike):
        print(*abc)
if muongi == 'U' or 'u':
    a = len(ilike)
    f = int(input('ban muon nang cap phan tu thu may?'))
    if f < a :
        ilike[f] = input('ban muon thay doi la gi?')
        print(ilike)
    elif f > a:
        print('phan tu thay doi ko phu hop')    
if muongi == 'D' or 'd':
    g = int(input('ban muon xoa phan tu thu may?'))
    a = len(ilike)
    if g < a:
        ilike.pop(g)
        print(ilike)
    elif g > a:
        print('phan tu muon xoa ko phu hop')
else:
    print('ban phai chon dung yeu cau')        



