print("*******************************************************")
print("********        file handling        *******************")
print("********************************************************")
import os
import sys
def fi():
    print("1. creat file ")
    print("2. list file ")
    print("3. edit file ")
    print("4. delect file ")
    print("5. read file ")
    print("6. program stopped ")
    a=input("enter your choice :")
    match a:
        case "1":
            print("____________________________________________")
            print(" creating file ")
            print("____________________________________________")
            print("enter your file name \n")
            f=input("")
            h=f+".txt"
            with open(h,'x')as file :
                print(f,"file is created successfully")
        case "2":
            print("____________________________________________")
            print("listing file ")
            print("____________________________________________")
            path="D:\gagan.n"
            file=os.listdir(path)
            for file in file:
                print(file)
        case "3":
            print("____________________________________________")
            print("editing file ")
            print("____________________________________________")
            name=input("enter the file name that you want to edit\n:")
            name=name+".txt"
            file=open(name,"a")
            print(file.write("world"))
        case "4":
            print("____________________________________________")
            print("deleting file ")
            print("____________________________________________")
            name=input("enter the file name that you want to delete\n:")
            name=name+".txt"
            os.remove(name)
            print("file",name,"deleted successfully")
        case "5":
            print("____________________________________________")
            print("reading file ")
            print("____________________________________________")
            print("reading file\n")
            print(".........................................\n")
            print("enter the file name that you want to read\n")
            f=input("")
            with open(f+".txt",'r')as file:
                print(file.read())
                print("the file read successfully\n")
        case "6":
            print("____________________________________________")
            print("program stopped ")
            sys.exit(0)
            print("____________________________________________")
while True:
    fi()
print("********************************************************")
        
     
    
