while True:
    n = input("so ban muon chon la gi?")
    if n.isalpha():
        print("ban phai nhap so")
        continue
    elif int(n) < 13:
        print("so ban chon be hon 13")
    elif int(n) == 13:
        print("so ban chon la so 13")
    else:
        print("so ban chon lon hon 13")
    