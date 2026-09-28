file = open("data.txt", "w") # r - read the file , w - write file (overwrite)
file.write("Hello Yogesh")   # a=append(add data),x-creat new file
file.close()   # file handling: FH is used to creat,read,read,writ and update file in python                                             





try:        #exception handling  is used to handle runtime errors using try and except blocks
    a = 10 
    b = 0
    print(a/b)
except:
    print("there is error")

    
try:
    num = int(input("Enter number: "))
    print(num)
except:
    print("Invalid input")
