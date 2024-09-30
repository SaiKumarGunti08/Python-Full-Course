#fibonacci Series of upto a perticular range
from itertools import count

list_A=[]
for i in range(0,11):
    summ=0
    if i<2:
        list_A.append(i)
    else:
        summ=list_A[-1]+list_A[-2]
        if summ>=10:
            break
        else:
            list_A.append(summ)
            summ += 0
print(list_A)
#fibonacci series
list_A=[]
for i in range(0,11):
    summ=0
    if i<2:
        list_A.append(i)
    else:
        summ=list_A[-1]+list_A[-2]
        list_A.append(summ)
        summ += 0
print(list_A)


#find the given number is a Prime Number or not
# number=int(input("Enter the Number : "))
# if number<=1:
#     print("Its not a Prime Number")
# else:
#     for i in range(2,(number//2)+1):
#         if number%i==0:
#             print('Not A prime number',i)
#             break
#         else:
#             print("Its a Prime number",i)

#palindrome
# number=int(input("Enter Number : "))
# number=str(number)
# number2=number[::-1]
# if len(number)<=1:
#     print("Number less than 10")
# else:
#     if number2==number:
#         print("Its a palindrome Number")
#     else:
#         print("Not A palindrome Number")

sentance="hello.sai.kumar.welcome.home"
sentance=sentance.split(".")
print(sentance)
sentance_2="hello sai"
print(sorted(sentance_2))
#for removing the value (directly we cant remove)
sentance_2=sentance_2.replace("e","")
print(sentance_2)

print(sentance_2.count("sai"))


