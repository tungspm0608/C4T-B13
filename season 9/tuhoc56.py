diemcao = [54,74,64,94,84]
them = int(input('ban muon them phan tu nao? '))
diemcao.append(them)
b = sorted(diemcao, reverse = True)
a = len(diemcao)
for i in range(5):
    print(b[i])

