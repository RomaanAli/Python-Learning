#loop practice in tuple
subjects = ("Math", "Physics", "English", "Programming")

for subject in subjects:
    print(subject)

i=0
while i < len(subjects):
    print(subjects[i])
    i+=1

#counting the numbers appear in the tuple
numbers = (10, 20, 30, 40, 20, 50, 20)
t = input("Enter the values in tuple separated by space:")
my_tuple = tuple(map(int,t.split()))
cout=0
c=0
for number in numbers:
    if number == 20:
        cout+=1
for i in my_tuple:
    if i == 20:
        c+=1

print("The number of time 20 appear in tuple:",cout)
print("The number of time 20 appear in tuple:",c)



