#importing os module, to work with paths.
import os

print(os.getcwd()) #gets current working directory

#changing the directory to the one with all TEXT files ONLY.
#The segregrating file types test was too confusing. working on it.
#A folder named "control script" on the Desktop containing the files.
os.chdir(r"C:\Users\MIR\Desktop\control script")
print(os.getcwd()) #check if it has changed the directory correctly.

#print(os.listdir())

#getting the files in the directory as a list, to append from, for iteration purpose.
f_exist=os.listdir()
print(f_exist)

#main block, where the magic happens.
#going through each file in the f_exist list, one by one.

for alone_file in f_exist:
    with open(alone_file,'r') as f: #opening files as f
        #print(alone_file) #prints file names
        f_contents=f.read() #reading the file and storing contents.
        with open('master.txt','a') as m: #creating a "master" the first time and then appending to that.
            m.write("\n"+"---" +"\n"+f_contents) #printing in the desired format.