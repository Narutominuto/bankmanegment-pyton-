Skip to content
shekar sheku
/
file-handling

Type / to search

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Commit
Add files via upload
 main
@shekar sheku
shekar sheku committed last week 
0 parents
commit b4b367f
Showing 1 changed file with 70 additions and 0 deletions.
 70 changes: 70 additions & 0 deletions70  
file handling.pyt.py
@@ -0,0 +1,70 @@
print("************************************************")
print("*            file handling                     *")
print("************************************************")
import os
import sys
def fi():
    print("1. create file")
    print("2.list file")
    print("3.edit file")
    print("4.delete file")
    print("5.read file")
    print("6.program stopped")
    a=input("enter your choice:")
    match a:
        case"1":
            print("___________________________________________")
            print("creating file")
            print("___________________________________________")
            print("enter your file name \n")
            f=input("")
            h=f+".txt"
            with open(h,'x')as file :
                print(f,"files is created successfully")
        case"2":    
            print("___________________________________________")
            print("listing file")
            print("___________________________________________")
            path="D:\Python Sql Connector"
            file=os.listdir(path)
            for file in file:
                print(file)
        case"3":    
            print("___________________________________________")
            print("editing file")
            print("___________________________________________")
            name=input("enter the file name that you want to edit\n:")
            name=name+".txt"
            file=open(name,"a")
            print(file.write("word"))
            print("edited the file")
        case"4":    
            print("___________________________________________")
            print("deleting file")
            print("___________________________________________")
            name=input("enter the file name that you want to delete\n:")
            name=name+".txt"
            os.remove(name)
            print("file",name,"deleted successfully")
        case"5":
            print("___________________________________________")
            print("reading file")
            print("___________________________________________")
            print("reading file\n")
            print("...........................................")
            print("enter the file name that you want to read\n")
            f=input("")
            with open(f+".txt",'r')as file:
                print(file.read())
                print("the file read successfully\n")
        case"6":
            print("___________________________________________")
            print("program stopped")
            sys.exit(0)
            print("___________________________________________")
while True :
    fi()
print("*******************************************************")



