n=int(input("Enter total number of terms:"))
L=[]
for i in range(n):
    num=int(input("Enter a number:"))
    L.append(num)
print("You have entered the following list:",L)
E=[]
for i in L:
 if i not in E:
     E.append(i)
L=E
print("Unique values of the list:",L)
