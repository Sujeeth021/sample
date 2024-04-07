a=567
b=0
for i in range(2,a//2):
    if(a%i==0):
        print(i," is not a Prime")
        b=1
        break
if b==0:
    print(i,"is Prime")