diemcao = [54,74,64,94,84]
them = int(input('ban muon them phan tu nao? '))
diemcao.append(them)
b = sorted(diemcao, reverse= True)
for i,a in enumerate(b):
    print(i+1 ,a,sep = ' ')


