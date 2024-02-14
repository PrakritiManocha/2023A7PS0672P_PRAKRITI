def bubblesort(L):
    for i in range(len(L)-1):
        flag=0
        for j in range(len(L)-i-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
                flag=1
                if flag==0:
                    break
    print("Second Largest element")
    print(L[-1])
n=int(input("Enter total number of elements:"))
L=[]
for i in range(n):
    m=input("Enter element of a list:")
    L.append(m)
print("Your entered list is:",L)
bubblesort(L)
