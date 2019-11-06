thumatoithich2 = ['truyen tranh','game']
a = int(input('ban muon xoa phan tu nao? '))
if a == 0:
    thumatoithich2.pop(0)
elif a == 1:
    thumatoithich2.pop(1)  
else:
    print('ko co phan tu phu hop de xoa')  


print(thumatoithich2)
