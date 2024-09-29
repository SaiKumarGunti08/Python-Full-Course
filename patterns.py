for i in range(1,6):
    print(i*"* ")

for i in range(1,6):
    print((str(i)+" ")*i)

for i in range(1,6):
    for j in range(1,i):
        print(j,end=" ")
    print()
print()

n=6
for i in range(1,n):
    op=(str(n-i)+" ")*(n-i)
    print(op)

for i in range(1,7):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
print()

n=5
for i in range(1,n):
    op="  "*(n-i)+(" *"*i)
    print(op)
print()
n=5
for i in range(1,n):
    op=" "*(n-i)+(" *"*i)
    print(op)
print()

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print()

for i in range(1,5):
    print(i*"* ")
for i in range(5,0,-1):
    print(i*"* ")
print()


for i in range(1,11):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()
print()
