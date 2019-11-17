tenquan = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
sodan = [150300, 247100, 333300, 266800, 420900, 318000]
b = sodan[0]
for i in sodan:
    if b < i:
        b = i
    else:
        pass
print(b)
c = sodan[0]
for x in sodan:
    if c > x:
        c = x
    else:
        pass
print(c)  