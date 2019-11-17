bangmau = [1,2,3]
bangmau[0] = 'green'
bangmau[1] = 'blue'
bangmau[2] = 'red'
d = input('ban muon xem cai gi?')
if d.isalpha:
    print('sai r nhap lai')
elif d < 3:
    print(bangmau[int(d)])
else:
    print('phan tu ban xem ko hop le')
