#print text
print('Hello world')

#variables
x = 5
y = "John"
print(x)
print(y)

#Get the variable type
print(type(x))
print(type(y))

#Assign Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Assign One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#collections
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Boolean
print(10 > 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#Operators
print(10 + 5)

#Operator Precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)
