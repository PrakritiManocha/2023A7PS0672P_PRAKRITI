n=int(input("Enter the total numbers of terms:"))
count=2
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a,b,end=" ")
else:
    print(a,b,end=" ")
    while count<=n:
        c=a+b
        print(c,end=" ")
        a,b=b,c
        count=count+1
