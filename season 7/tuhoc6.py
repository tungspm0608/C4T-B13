from turtle import * 
shape('turtle')
while True:
    bk = input('ban muon chon bk la bao nhieu?')
    if bk.isalpha():
        continue
    circle(int(bk))
    break
mainloop()