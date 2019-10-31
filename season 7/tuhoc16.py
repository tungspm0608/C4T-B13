while True:
    tendangnhap = input("ten dang nhap cua ban la?")
    matkhau = input("mat khau cua ban la?")
    if len(matkhau) < 8 and matkhau.isalpha:
        print("ko du 8 ki tu nhap lai")
        continue
    nhaplaimatkhau = input("xac nhan lai mat khau cua ban?")
    if matkhau != nhaplaimatkhau:
        print("xac  nha mat khau ko dung vui long nhap lai")
        continue
    email = input("email cua ban la ?")
    if '@gmail.com' in email:
        print('dang ki thanh cong')
        continue
    else:
        print("email ko hop le")


