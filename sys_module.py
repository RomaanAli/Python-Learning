import sys

print("\nVersion : ",sys.version)
print("Version_Info : ",sys.version_info)

print("\nThe sys.argv[0] is script name: ",sys.argv[0])
print("Arguments are:")
for i in sys.argv:
    print(i)

name= str(sys.stdin.readline())
print(name)

print("The size of  just enter named by Stdin.readline: ",sys.getsizeof(name))

