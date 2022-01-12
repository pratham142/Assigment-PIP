##20CE158 Pratham Patel
##Github Repository Link
##https://github.com/pratham142/Assigment-PIP
##Dictionaries
##(a)
d1 = {0:10,1:20,2:30,3:40}
d2 = {4:50,5:60}
try:
    n = int(input())
except ValueError:
    print("Enter Integer Value")
try:
    if n in d1:
        print("Key already exists")
    else:
        print("Key doesn't exist")
except NameError:
    pass
##(b)
d3 = {**d1, **d2}
##(c)
s = 0 
for i in range(len(d3)):
    s += d3[i]
print(s)
##(d)
q = int(input("Enter key: "))
p = int(input("Enter value: "))
d3[q] = p
##(e)
d1.update(d2)
d1.update(d3)
print(d1)
##Tuple
##(a)
t1 = ("Charusat University",1,12.25)
print(t1)
##(b)
t2 = (1,2,3,4,5)
print(t2[4])
##(c)
k = int(input("Enter a number: "))
l = list(t2)
l.append(k)
t2 = tuple(l)
print(t2)
##(d)
s = str(t1)
print(type(s))
##(e)
print(len(t1))
##Set
##(a)
s1 = {1,2,3,4,5}
a = int(input("Enter a number: "))
s1.add(a)
print(s1)
s1.clear()
print(s1)
##(b)
s1 = {1,2,3,4,5}
b = int(input("Enter a number: "))
if b in s1:
    s1.remove(b)
else:
    pass
print(s1)
##(c)
s2 = {3,4,5,6,7}
print(s1.intersection(s2))
print(s1.union(s2))
print(s1 - s2)
print(s2 - s1)
##(d)
print(max(s1), min(s1))
##(e)
list = [1,2,2,2,4,4,4,4,5]
tuple = (3,3,4,4,4,5,5,5,5)
dict = {1:5,2:5,3:6,4:7,5:7,6:7,7:7}
dict1 = {}
for i in range(0,len(list)):
    print(list.count(list[i]))
for i in range(0,len(tuple)):
    print(tuple.count(tuple[i]))
for key,values in dict.items():
    if values not in dict1:
        dict1[values] = [key]
    else:
        dict1[values].append(key)
print(str(dict1))
        
