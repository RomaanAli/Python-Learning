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
"""
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