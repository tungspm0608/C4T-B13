banggia = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 1200,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJITSU' : 900,
    'ALIENWARE' : 1000    
}
cacmay = {
    'HP' : 20,
    'DELL' : 60,
    'MACBOOK' : 10,
    'ASUS' : 30,
    'TOSHIBA' : 10,
    'FUJITSU' : 15,
    'ALIENWARE' : 5
}
print('bang gia cua ASUS la: ',banggia['ASUS'])
a = input('ban muon xem loai may gi: ')
if a in banggia:
    print('bang gia cua may ban chon la: ',banggia[a])
else:
    print('ko co thong tin')    
print('5 may ASUS co gia tri la:',banggia['ASUS'] * 5)  
banmuondaysola = input('day so ban muon mua may gi va so luong la:')
chonloc = banmuondaysola.split(':')
if chonloc[0] in banggia and chonloc[1].isalpha:
    print('voi loai may la: ',chonloc[0],'co so luong la: ',chonloc[1], 'tong so tien la: ',banggia[chonloc[0]]*int(chonloc[1]))
    cacmay[chonloc[0]] =  cacmay[chonloc[0]] - int(chonloc[1]) 
    print('so luong may con lai la:',cacmay)
else:
    print('so luong hoac loai may ko hop le')   
            
