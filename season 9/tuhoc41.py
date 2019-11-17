colours = ['blue', 'green', 'yellow','Dark', 'white']

while len(colours) != 0:
    d = input('ban muon chon cai gi: ')
    if d.isdigit():
        print('Pop ',d,' (',colours[int(d)],')')
        colours.pop(int(d))
    elif d.isalpha():
        isIn = False
        for i in colours:
            if i == d:
                colours.remove(i)
                print('Remove ',d)
                isIn = True
                break
        if isIn == False:
            print('ko hop li ',d)
    else:
        print('nhap sai!!!')
    print(colours)


        
       
