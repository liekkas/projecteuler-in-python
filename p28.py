s=0
for i in range(1001,1,-2):
    t = i**2
    for j in range(4):
        s += t - j * (i-1)
s+=1
print s