def list_get():
    li=[]
    for i in range(int(input("Enter how many numbers you want to enter:"))):
        li.append(int(input("Enter a number:")))
    return li
"""li=[10,20,30,40,50]
avg=sum(li)/len(li)
print(int(avg))
print(li)
ser=int(input("Enter a number want to search:"))
print(type(ser))
if ser in li:
    print("found in list")
else:
    print("not in list")

li=[]
for i in range(int(input("Enter how many numbers you want to enter:"))):
    li.append(int(input("Enter a number:")))
no=0
n=int(input("Enter a number to search:"))
for i in li:
    if i==n:
        no+=1
print(f"The ---{n}---  appears {no} times")

#li=[10,20,30,40,50]
li=[]
for i in range(int(input("Enter how many numbers you want to enter:"))):
    li.append(int(input("Enter a number:")))
print(li)
f=int(input("Enter a number to search:"))
ind=[]
for i,num in enumerate(li):
    if f==num:
        #print(f"found in list--{num}-- at the index **{i}**")
        ind.append(i)

print(f"the first occurrence is {ind[0]} and the last occurrence is {ind[-1]}")
print(f"These are all index where {f} occurs:",ind)

new=[]
missing=[]
list_get()
to_n=int(input("Enter n number to make a list:"))
for i in range(to_n+1):
    new.append(i)
for i in new:
    if i not in li:
        missing.append(i)
missing.sort()
print("missing values are:",missing)

l1=list_get()
print(l1)
l2=list_get()
print(l2)
l3=l1+l2
l3.sort()
print("The merge of these list are:",l3)
common=[]
for i in l1:
    if i in l2:
        common.append(i)
common.sort()
print("The common elements in both list are:",common)

l1=list_get()
pairs=[]
target=int(input("Enter the target number:"))
for i in l1:
    for j in l1:
        if target==i+j:
            pair=(i,j)
            pairs.append(pair)

print(pairs)

l1=list_get()
zeros=[]
nonzero=[]
zero=0
print(l1)
for i in l1:
    if i == 0:
        zeros.append(i)
        zero += 1
    else:
        nonzero.append(i)
l1=nonzero+zeros
print("The number of zeros are:",zero)
print("the 0 goes to at the end:",l1)


l=list_get()
zeros=[]
nonzero=[]
[zeros.append(i) if i==0 else nonzero.append(i) for i in l]
l=nonzero+zeros
print("new list is",l)
"""
#l=list_get()
l=[2,3,2,4,2,2,0,2]
n=int(input("Enter a number to search:"))
count = sum(1 for i in l if i == n)
print(f"The ---{n}---  appears {count} times")

