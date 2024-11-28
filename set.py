#Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Get the Length of a Set
print(len(thisset))

#Set Items - Accept multiple Data Types
set1 = {"abc", 34, True, 40, "male"}

#Access Set Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

print("banana" in thisset)
print("banana" not in thisset)

#Add Single Set Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Add Multiple Set Items
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Remove Item - remove() method
#Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Remove Item - discard() method
#Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)