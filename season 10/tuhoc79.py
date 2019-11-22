tongsocaudung = 0
f = {
    'cau hoi' : 'hang san suat phim thuy hu la gi?',
    'ban hay' : 'chon 1 trong 4 phuong an sau:',
    'a:' : 'trung quoc',
    'b:' : 'nhat ban',
    'c:' : 'han quoc',
    'd:' : 'ko co dap an'
}
for ac,acc in enumerate(f):
    print(acc,f[acc])
g = input('dap an cua ban la: ')
if g == 'a':
    tongsocaudung += 1
    print('dung r',' ','tong so cau dung =',tongsocaudung,' ','phan tram tra loi dung la=',100)
else:
    print('sai r','        ','tongsocaudung=',tongsocaudung,' ','phan tram tra loi dung la',0)    
f['cau hoi'] = 'thuy hu phat hanh nam bao nhieu'
f['a:'] = '1911'
f['b:'] = '1922'
f['c:'] = '1933'
f['d:'] = '1944'
for ac,acc in enumerate(f):
    print(acc,f[acc])
g = input('dap an cua ban la: ')
if g == 'b':
    tongsocaudung += 1
    print('dung r','        ','tong so cau hoi dung la=',tongsocaudung,' ','phan tram tra loi dung la',100)
else:
    print('sai r','         ','tong so cau hoi dung la=',tongsocaudung,' ','phan tram tra loi dung la',50)   
