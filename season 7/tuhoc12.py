while True:
    n = input("so ban muon chon la gi?")
    if int(n) < 0:
        print("so am ko le cung ko chan")
        continue
    elif int(n) % 2 == 0:
        print("so ban chon la so chan")
    else:
        print("so ban chon la so le")    