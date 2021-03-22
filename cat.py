# IMPLIMENTATION OF CAT FUNCTION IN PYTHON

def read():
    f = input("ENTER THE FILE LOCATION YOU WANT TO READ : ")
    file = open(f,'r')
    if file.mode == "r":
        content = file.read()
        print(' ')
        print(content)
        print(' ')
    else:
        print("FILE LOCATION INVALID")

def write():
    f = input("ENTER THE FILE LOCATION YOU WANT TO WRITE : ")
    file = open(f,'a+')
    if file.mode == "a+":
        content = input("ENTER THE CONTENT TO BE ADDED : ")
        file.write("\n"+str(content))
    else:
        print("FILE LOCATION INVALID")

def create():
    f = input("ENTER THE FILE LOCATION YOU WANT TO CREATE FILE IN : ")
    name = input("ENTER THE NAME OF YOUR TEXT FILE : ")
    fname = str(f)+"/"+str(name)+".txt"
    file = open(fname,'w+')
    if file.mode == "w+":
        content = input("ENTER THE CONTENT TO BE ADDED : ")
        file.write(content)
        print(" ")
    else:
        print("FILE LOCATION INVALID")




def main():
    print('\nCHOOSE THE ACTION YOU WANNA PERFORM ON THE FILE: \n1.READ \n2.WRITE \n3.CREATE A NEW FILE \n')
    option=int(input("\nENTER YOUR CHOICE : "))
    print('')
    if(option==1):
        read()
    elif(option==2):
        write()
    elif(option==3):
        create()
    else:
        print("CHOOSE A VALID OPTION")

if __name__ == "__main__":
    main()
      