#check number is positive or not
# num=int(input("enter number : "))
# if num>0:
#     print('positive')
# elif num==0:
#     print('Zero')
# else:
#     print('negative')

#odd or even
number=int(input("Enter the number : "))
print('Its an even') if number%2==0 else print('its an odd')

#calculate the area
# print('********* AREA CALCULATION **********')
# print("""Press 1 to get the area if square
# Press 2 to get area of rectangle
# Press 3 to get area of Triangle
# press 4 to get area of circle""")
# choosen_number=int(input("Enter The number between 1-4 : "))
# if choosen_number==1:
#     one_side=float(input('Enter the length of one side :'))
#     square=one_side**2
#     print("The area of square is : ",square)
# elif choosen_number==2:
#     length=float(input("enter Length of Rectangle : "))
#     width=float(input("enter width of rectangle : "))
#     areaOfRectangle=length*width
#     print('The area of rectange is : ',areaOfRectangle)
# elif choosen_number == 3:
#     length = float(input("enter Length of Triangle : "))
#     base = float(input("enter Base of Triangle : "))
#     areaOfTriangle = (length * base)/2
#     print('The area of Triangle is : ', areaOfTriangle)
# elif choosen_number==4:
#     radious=float(input("Enter radious for the circle : "))
#     circle_area=((22/7)*(radious**2))
#     print('The area of circle is : ',circle_area)
# else:
#     print("Invalid Input","you had choose : ",choosen_number,"choose number between  1-4")


#vowels or not
letter=input("Enter a letter : ")
vowels="AaEeIiOoUu "
num='1234567890@,#/*&^%$!()_-=+'
# print(letter," is a vowel") if letter in vowels else print(letter,"is a consonant")
if letter in vowels:
    print(letter,"is a vowel")
elif letter in num:
    print("Enter a valid input You had entered : ",letter)
else:
    print(letter, "is consonant")
