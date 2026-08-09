import os
"""
def list_all_files():
    ld=os.listdir(os.getcwd())
    print("---listing all files of the directory----")
    for i in ld:
         print("  ",i)

def file_size(fn):
    return os.path.getsize(fn)


cd=os.getcwd()
print("\nThe current directory is:",cd)
print("----Changing directory to new-----")
os.chdir("D:\\Degree\\FYP")
print("New directory is:",os.getcwd())
os.chdir("D:\\Grayphite\\Python-Learning")

list_all_files()
print(os.name)

for i in os.listdir(os.getcwd()):
    print(f"The size of --{i}-- is :{file_size(i)}")

#s.mkdir("New_Directory")
#os.chdir("New_Directory")
print(os.getcwd())
os.rmdir("NEw_Directory")
print(os.getcwd())
print(os.listdir())

"""
#os.mkdir("TEST_DIRECTORY")
os.chdir("TEST_DIRECTORY")
print(os.getcwd())
os.makedirs("parent//child",exist_ok=True)

print(os.getcwd())
print(os.path.exists("D:\\Grayphite\\Python-Learning\\TEST_DIRECTORY\\parent\\child"))

print(os.path.isdir("D:\\Grayphite\\Python-Learning\\TEST_DIRECTORY"))
os.makedirs("parent//child",exist_ok=True)
os.chdir("parent//child")
print(os.getcwd())
print(os.listdir())
#os.rmdir("D:\\Grayphite\\Python-Learning\\TEST_DIRECTORY\\parent\\child")
#os.renames("test.txt","NEW.txt")
print("-----",os.listdir())
