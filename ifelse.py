#If example
a = 33
b = 200
if b > a:
  print("b is greater than a")

#If else example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#If elif else example
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")