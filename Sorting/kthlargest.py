l=[6,7,3,4,5,2,3,4,8,2,9]
n=len(l)
print(n)
k=5
c=1
for i in range(n-1):
    flag=False
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            flag=True
    if c==k:
        break
    c+=1
    print(l)
    if not flag:
        break

print("Final",l)
print(l[n-k],l[-k])