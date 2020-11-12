print("enter your number")
num1=int(input())
print("enter your number")
num2=int(input())
print('enter your choice '+' +,-,*,/,%')
num3=(input())
if  (num1==45 and num2==3 and num3=='+'):
    print("100")

elif (num1==45 and num2==3 and num3=='%'):
    print("2")

elif (num1==45 and num2==3 and num3=='-'):
     print(6)
elif num3 == '*':
     num4 = num1 * num2
     print(num4)
elif num3 == '+':
    plus = num2 + num1
    print(plus)
elif num3 == '/':
    Dev = num2 / num1
    print(Dev)
elif num3 == '-':
    Dev = num2 - num1
    print(Dev)
elif num3 == '%':
    percent = num2 % num1
    print(percent)
else:
    print("Error! Please check your input")