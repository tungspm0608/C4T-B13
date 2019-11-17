a = [49, 100, 33, 89, 41]
b = sorted(a,reverse=True)

# print and enter high score
print("High score:")
for i, x in enumerate(b):
    print(i+1,x,sep=".")

for y in range(len(b)):
    if y < len(b)-1:
        pass
    else:
        c = int(input("Enter your new high-score: "))

#final arrangement
b.append(c)
d = sorted(b,reverse=True)
for e,f in enumerate(d):
    print(e+1,f,sep=".")
