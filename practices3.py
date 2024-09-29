#sum of first n numbers
n=int(input("Enter number : "))
ssum=0
for i in range(1,n+1):
    if i%2==0:
        ssum+=i
        #print(i)
print(ssum)

#print till 20 and their squares

for i in range(1,21):
    print(i," :-",i**2)
print()

#print sum of odd numbers using while
sum2=0
n=0
while n<=20:
    if n%2!=0:
        sum2+=n
        #print(n)
    n+=1
print(sum2)

for i in range(1,101):
    if i%8==0 and i%12==0:
        print(i,end=" ")
print()
