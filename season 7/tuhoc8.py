while True:
    n = input("so ban nmuon chon la gi?")
    if int(n) < 0:
        print("sai r nhap lai")
        continue
    for i in range(0,int(n)+1):
        print(i)