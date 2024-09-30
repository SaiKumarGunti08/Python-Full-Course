#calculate the area
print('********* AREA CALCULATION **********')
while True:
    print("""Press 1 to get the area if square
    Press 2 to get area of rectangle
    Press 3 to get area of Triangle
    press 4 to get area of circle""")
    choosen_number=int(input("Enter The number between 1-4 : "))
    if choosen_number==1:
        while True:
            one_side=float(input('Enter the length of one side :'))
            square=one_side**2
            print("The area of square is : ",square)
            repete=input(" Do you want to repete the square : (Yes / No) :")
            if repete=="No"  or repete=="no":
                break
    elif choosen_number==2:
        while True:
            length=float(input("enter Length of Rectangle : "))
            width=float(input("enter width of rectangle : "))
            areaOfRectangle=length*width
            print('The area of rectange is : ',areaOfRectangle)
            repete = input(" Do you want to repete the rectangle : (Yes / No) :")
            if repete == "No"  or repete=="no":
                break
    elif choosen_number == 3:
        while True:
            length = float(input("enter Length of Triangle : "))
            base = float(input("enter Base of Triangle : "))
            areaOfTriangle = (length * base)/2
            print('The area of Triangle is : ', areaOfTriangle)
            repete = input(" Do you want to repete the triangle : (Yes / No) :")
            if repete == "No"  or repete=="no":
                break
    elif choosen_number==4:
        while True:
            radious=float(input("Enter radious for the circle : "))
            circle_area=((22/7)*(radious**2))
            print('The area of circle is : ',circle_area)
            repete = input(" Do you want to repete the circle : (Yes / No) : ")
            if repete == "No" or repete=="no":
                break
    else:
        print("Invalid Input","you had choose : ",choosen_number,"choose number between  1-4")
    repete=input("Do You wamt to repete the process: (Yes / No) :")
    if repete=="no" or repete=="No":
        break

