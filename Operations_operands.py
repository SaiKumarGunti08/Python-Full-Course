#arthematic operators are
#Add=1+2
# sub=1-2
# mult=2*4
# div=4/2
# modulus=2%4 (reminder)
# floor dividion=2//4  (questient)
# exponentiation=2**4
from operator import is_not

print('arthematic operator')
print(8/3)
print(8//3)
print(8%3)
print(2*4)
print(2+2)
print(3-2)

#comparison Operator
print('comparison operator')
print(3>2)
print(3<2)
print(3==2)
print(3==3)
print(3<=2)
print(3<=3)
print(3>=2)
print(3!=2)

#logical Operator //and (x and y) //or (x or y) //  not (not x)
print('logical operatior')
print(3>2 and 3==3)
print(3>2 or 3<2)
print(not 3==3)
print(not 3!=3)

#Assigment Operator
print('Assigment operators')
score=2
print(score)
score+=1
print(score)
score-=1
print(score)
score*=2
print(score)

#identity operator checks the data type same or not
print('identical operator')
num1=111
#num2='111'
num2=12
print(num1 is num2)
print(num1 is not num2)

#bitwise Operators
print('bitWise operators')
print('AND &')
print(0&0)#=0
print(1&0)#=0
print(0&1)#=0
print(1&1)#=1

print('OR | ')
print(0|0)#=0
print(1|0)#=1
print(0|1)#=1
print(1|1)#=1

print('XOR ^')
print(0^0)#=0
print(1^0)#=1
print(0^1)#=1
print(1^1)#=0

print(bin(10),'binary number')


#Membership Operatior (to find the presses or not) //in // not in
print('Membership Operator')

name="saiAparna"
print("z" in name)
print("a" in name)
print("z" not in name)
print("a" not in name)


