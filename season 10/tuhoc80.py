while True:
    f = {
        'cau hoi' : 'con bach tuoc co bao nhieu chan?',
        'ban hay' : 'chon 1 trong 4 phuong an sau:',
        'a:' : '1',
        'b:' : '2',
        'c:' : '4',
        'd:' : '8'
    }
    for ac,acc in enumerate(f):
        print(acc,f[acc])
    g = input('dap an cua ban la: ')
    if g == 'd':
        print('dung r')
        break
    else:    
        print('sai r')   
