while True:
    a = input("so ban muon chon la gi?")
    if a.isdigit():
        print(int(a)*int(a))
    elif a.isalpha():
        print('sai r nhap lai')
    break 
