# num1 = float(input("Enter your first number"))
# num2 = float(input("Enter your second number"))
# num3 = float(input("Enter your third number"))

# average = num1 + num2 + num3 /3
# print("The average of {0} , {1} and {2} is = {3:.2f} ".format(num1,num2,num3,average))

# if(average >= 75):{
#     print("Excelent")
# }
# elif(50 <= average <=75):{
#     print("Satisfied")
# }
# else :{
#     print("poor")
# }





# Area of a rectangle

# side = int(input("enter square side :"))

# print("area :", side*side)

# num1 =int(input("enter your number"))
# squareroot = num1 ** 0.5
# print("The square root of the {0} is : {1}".format(num1,squareroot))

# import cmath
# num = 10 - 3 + 10j  + 5j
# squareroot = cmath.sqrt(num)
# print("The square root of {0} is : {1:.2f} and {2:.2f}".format(num,squareroot.real,squareroot.imag))






# a = int(input("Enter first number "))
# b = int(input("Enter second number "))
# c = int(input("Enter third number "))

# side = (a + b + c) /2
# area = (side*(side-a)*(side-b)*(side-c))**0.5

# print("The area of a triangle is {0:.2f} square.fit ".format(area))







# celsius = int(input("enter your temperature in degree"))
# fahrenheit = (celsius * 9/5) + 32
# print("{0:.2f} celsius gedree  is equal to = {1:.2f} fahrenheit degree ".format(celsius,fahrenheit))







# degree = int(input("Enter your degree"))
# method = (input("Enter your value in celsius and fahrenheit"))

# if method == "cel":
#    fahrenheit = (degree * 9/5) + 32
#    print("The fahrenheit of {0} = {1} celsius".format(degree,fahrenheit))
# elif method == "far":
#     celsius=(degree-32)*5/9
#     print("The celsius of {0} = {1} fahrenheit".format(degree,celsius))






# import cmath

# a = int(input("value of a = "))
# b = int(input("value of b = "))
# c = int(input("value of c = "))

# f = (b**2) - (4 * a * c)

# sol1 = -b + cmath.sqrt(f) /2 * a
# sol2 = -b - cmath.sqrt(f) /2 * a

# print("a = {0}, b = {1}, c = {2} The solution are {3:.2f} and {4:.2f}".format(a,b,c,sol1,sol2))








# multiplier = 11
# count = 1

# while count <= 10:
#     result = count * multiplier
#     print(f"{multiplier} * {count} = {result}")
#     count += 1



# n = int(input("Enter your number  =  "))

# if (n%2 == 0):
#     print("This number is even ")

# else:
#     print("This number is odd")





# a = int(input("Enter a number"))
# b =int(input("Enter your number"))
# c =int(input("Enter your number"))

# if (a>b ,a>c):
#     print("gratest number is a = ")

# elif(b>a , b>c):
#     print("gretest number is b =")    

# else (c>a , c>b):
#     print("gretest number is c =")



num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

result = num1 + num2
print(f"{num1} + {num2}  = {result}")
