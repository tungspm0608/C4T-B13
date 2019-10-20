while True:
    matkhau = input('what is your pass?')
    print(matkhau)
    print(len(matkhau))
    if len(matkhau) < 8:
        print("ko du 8 ki tu loai")
    elif matkhau.isdigit():
        print('dung roi')

        break   
    else:
        print("sai r nhap lai")

