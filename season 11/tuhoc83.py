banggia = {
    'HP' : [20,600],
    'DELL' : [60,650],
    'MACBOOK' : [10,1200],
    'ASUS' : [30,400],
    'ACER' : [10,350],
    'TOSHIBA' : [10,600],
    'FUJITSU' : [15,900],
    'ALIENWARE' : [5,1000]    
}
b = 0
for a in banggia.values():
    b += a[0]*a[1]
print('tong tai san cua cua hang la',b)

