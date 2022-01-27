# simple calculator in python
# function to add two numbers
def addition(num1,num2):
    return num1 + num2
#function to subtract two numbers
def subtraction(num1,num2):
    return num1-num2
#function to multiply two numbers
def multiplication(num1,num2):
    return num1*num2
#function to divide two numbers
def division(num1,num2):
    return num1/num2
print("please select operation -\n" \
        "1. addition\n" \
        "2. subtraction\n" \
        "3. multiplication\n" \
        "4. division\n")
#take input from the user
select = int(input("select operations from 1,2,3,4 :"))
number_1 = int(input("enter first number: "))
number_2 = int(input("enter second number: "))
if select == 1:
    print(number_1,"+",number_2,"=",
                    addition(number_1,number_2))
elif select == 2:
    print(number_1,"-",number_2,"=",
                    subtraction(number_1,number_2))
elif select == 3:
          print(number_1,"*",number_2,"=",
                    multiplication(number_1,number_2))
elif select == 4:
         print(number_1,"/",number_2,"=",
                    division(number_1,number_2))
else:
    print("invalid input")
    
          

    
    
    
    
