while True:
    matkhau = input('what is your pass?')
    print(matkhau)
    if matkhau.isdigit():
        print(len(matkhau))
    if len(matkhau) < 8:
        print("ko du 8 ki tu loai")
    elif matkhau.isdigit():
        print('dung roi')

        break   
    else:
        print("mat khau khong dung / phai la chu so")

