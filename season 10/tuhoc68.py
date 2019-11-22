tudienanhviet = {
    "hello" : "xin chao",
    "hi" : "xin chao",
    "look" : "nhin kia",
    'WOW' : 'tuyet voi'
}
while True:
    c = input('ban muon xem cai gi?    ')
    if c  in tudienanhviet:
        print(c,'co nghia la',tudienanhviet[c])
    else:
        print(c ,'ko co o trong tu dien')    