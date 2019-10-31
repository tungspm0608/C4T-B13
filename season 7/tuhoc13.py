while True:
    thang = int(input('thang may?'))
    if thang == 1 or thang == 3:
        print('la mua xuan co 31 ngay')    
    elif thang == 2:
        print('la mua xuan co 29 ngay')
    elif thang == 4 or thang == 6:
        print('mua he va co 30 ngay')
    elif thang == 5:
        print ('la mua he va co 31 ngay')      
    elif thang == 7 or thang == 9:
        print('mua thu va co 31 ngay')
    elif thang == 8:
        print ('la mua thu va co 30 ngay')      
    elif thang == 10 or thang == 12:
        print('mua dong va co 30 ngay')
    elif thang == 11:
        print ('la mua dong va co 31 ngay')  
    else:
        print("ko la mua gi ca")     