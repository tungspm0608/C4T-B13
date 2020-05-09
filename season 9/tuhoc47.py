banmuondaysola = input('day so ban muon la (cach boi dau ' ')?')
chonloc = banmuondaysola.split(' ')
for i in chonloc:
    s = 0
    s += int(i)
    if s % 2 == 0:
        print(s)
    else:
        print('so nay ko chia het cho 2')    