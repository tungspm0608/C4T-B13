n = [1,5,8,12]
for i in n:
    sums = 0
    sums += i
    if sums % 2 == 0:
        print(sums)
    else:
        print('phan tu ko chi het cho 2 o day la :  ',n.index(sums))
    