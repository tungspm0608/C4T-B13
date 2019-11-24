thongtin = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}
print(thongtin['MACBOOK'])
a = input('so ban muon xem la gi? ')
if a  == 'HP':
     print('so luong co trong kho la',thongtin['HP'])
if a == 'DELL':
    print('so luong co trong kho la',thongtin['DELL'])
if a == 'ASUS':
    print('so luong co trong kho la',thongtin['ASUS']) 

else:
    print('cai do ko co trong kho')  
thongtin['TOSHIBA'] = 10
b = input('ban muon them may gi? ')
c = input('so luong loai may ban them vao la bao nhieu? ')
thongtin[b] = c
thongtin['DELL'] = 10
thongtin['MACBOOK'] = 2
print('so luong MACBOOK co trong kho la:',thongtin['MACBOOK'])
e = 0
for i in thongtin.values():
    e += int(i)
print('tong so may o kho la: ',e)
thongtin['FUJITSU'] = 15
thongtin['ALIENWARE'] = 5
g = 0
for f in thongtin.values():
    g += int(f)
print('tomg so may trong kho la: ',g)     