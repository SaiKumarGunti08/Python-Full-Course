#loops //repeating the number
#for Loop
# number=int(input("Enter the Number : "))
# for i in range(1,number+1,2):
#     print("saiAparna",i)
# number=int(input("Enter the Number : "))
# for i in range(1,number+1):
#     print("saiAparna",i)
#
print('*********** Mathematical Table ************')

frstNum=int(input("Enter the Table You Want : "))
#
for i in range(1,10+1):
    print(frstNum,"X",i,"=",frstNum*i)
#
#
# #while loop // while loop executes the loop till the condition is True
# i=0
# while i<=10:
#     print(i)
#     i+=1

#Nested Looping

for i in range(1,4):
    for j in range(1,11):
        print(j,end="")
    print()

i=5
for i in range(1,i+1):
    print(("* ")*i)

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()