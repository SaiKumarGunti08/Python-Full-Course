a=""
b=""
c=""
for i in range(1,21 ):
    if i%2==0:
        a+=str(i)+" "
    elif i%3==0:
        b+=str(i)+" "
    else:
        c+=str(i)+" "
print(a)
print(b)
print(c)


#prime numbers
for i in range(1,11):
    if i%1==1 and i%i==0:
        print(i,end=" ")
print()

#using continue  //skips
for i in range(1,11):
    if i==3 or i==5:
        print("this value  is skipped")
        continue
    else:
        print(i)
print()

#break
for i in range(1,11):
    if i==7:
        print("this value is skipped")
        break
    else:
        print(i)
print("loop is ended at 7")

