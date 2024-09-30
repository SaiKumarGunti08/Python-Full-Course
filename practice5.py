#reverse the string
strings=input("enter the string : ")
strings=strings[::-1]
print(strings)

strings_2="11111"
b=strings_2.isdigit()
print(b)

stng='hello sai am from hyderabad'
vowels="AaEeIiOoUu"
counts=0
for i in stng:
    if i in vowels:
        counts+=1
print(counts)
