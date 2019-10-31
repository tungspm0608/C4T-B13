while True:
    n = input("so ban nmuon chon la gi?")
    if int(n) < 0:
        print("sai r nhap lai")
        continue
    for i in range(1,int(n),2):
        print(i)