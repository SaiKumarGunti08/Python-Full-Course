a=['sai','aparna','chinnu','chintu']
#swap sai and chintu
a[0],a[3]=a[3],a[0]
print(a)
a.insert(2,"chinni")
print(a)
a[0],a[4]=a[4],a[0]
print(a)
#delete
a.pop(2)
print(a)
b=[1,5,3,2,4]
b.sort()
print(b)
multi=1
for i in b:
    multi*=i
print(multi)
print(max(b))
print(min(b))