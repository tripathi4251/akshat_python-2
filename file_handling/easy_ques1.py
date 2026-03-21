#create a new file practice.txt using python.." add the following data on it..
#hi everyone
#we are learning file I/O using python..
#i like programming in python..

f=open("practice.txt","w")
f.write("hi everyone")
f.close()

f=open("practice.txt","a")
f.write("\n we are learning file I/O using python.." 
        "\n i like programming in python..")
f.close()