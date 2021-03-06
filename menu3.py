import os
import cv2
import getpass
import subprocess as sp
os.system("tput setaf 1")
print('\t\tWelcome to my TUI to make your life easy\t\t')
os.system("tput setaf 7")
print("\t\t----------------------------------------\t\t")
##CHECKING PASSWORD TO LOGIN
getPass = getpass.getpass("Enter your default password = ")
checkPass = 'anmol'
if getPass != checkPass :
    os.system("tput setaf 1")
    print("Authentication Failed!!")
    os.system("tput setaf 7")
    exit()
##CHECKING LOCATION
print("Where you want to run the command (local/remote) =",end='')
location=input()
location1=location.lower()
if location1=='remote':
    IP=input("Enter IP to you want to connect = ")

print("""Press 1: Date
Press 2: Calendar
Press 3: Configure the Web Server
Press 4: Create User
Press 5: Create Direcory
Press 6: Create file
Press 7: Delete Directory
Press 8: Switch Host
Press 9: Stop the APACHE Web Server
Press 10: Start docker services
Press 11: Access CCTV live feed
Press 12: Exit
""")
repeat=input("To continoue press Y/N = ")
repeat1=repeat.lower()
while repeat1=='y' :

    print("Enter yor choice = ",end="")
    ch=input()

    if location1=='local':

    
        if int(ch)==1 :
            os.system("date")
        elif int(ch)==2 :
            os.system("cal")
        elif int(ch)==3:
            checkRpm = sp.getoutput('rpm -q httpd')
            check = 'package httpd is not installed'
            if checkRpm != check :
                print("Configuring the Web Server!")
                print("Starting the Web Server")
                os.system('systemctl start httpd')
                print("Web Server Started..")
            else :
                os.system('yum install httpd')
        elif int(ch)==4:
            userName=input("Enter your user name = ")
            os.system("useradd {}".format(userName))
            print("User created!!")
        elif int(ch)==5 :
            os.chdir('/root')
            os.system("ls")
            location=input("choose location = ")
            os.chdir('{}'.format(location))
            print("What is your Directory name = ",end="")
            name=input()
            os.system("mkdir "+ name)
            print("Directory Created")
        elif int(ch)==6:
            print("Enter your file name = ",end="")
            FileName=input()
            print("")
            os.system("touch "+ FileName)
            print("File Created")
        elif int(ch)==7:
            checkLoc = input("Where you want to Delete the fir from Root/Current = ")
            if checkLoc == 'current' :
                os.system('ls')
                print("Enter the directory name to Delete = ",end="")
                fileDel=input()
                os.system("rm -r "+fileDel)
                print("Dir Deleted")
            else :
                os.chdir('/root')
                os.system("ls")
                rootLoc = input("Where you want to go = ")
                os.chdir('{}'.format(rootLoc))
                os.system('ls')
                fileD = input('Enter the file name to Delete = ')
                os.system("rm -r {0}".format(fileD))
                print("Dir Deleted")
        elif int(ch)==9:
            os.system('systemctl stop httpd')
        elif int(ch)==10:
            os.system('systemctl start docker')
            os.system('tput setaf 5')
            os.system('docker images')
            os.system('tput setaf 7')
            inputImages = input("Enter the image namr to run = ")
            os.system('docker run -it {}'.format(inputImages))
            stopDoc = input("Do you want to stop Docker Services press y/n = ")
            if stopDoc == 'y':
                print("Stoping Docker")
                os.system('systemctl stop docker')
        elif int(ch)==11:
            cap = cv2.VideoCapture('http://192.168.1.5:8080/video')
            while True:
                status, photo = cap.read()
                cv2.imshow('hi',photo)
                if cv2.waitKey(1) == 27:
                    break
            cv2.destroyAllWindows()
            cap.release()
        elif int(ch)==12:
            print("Exiting the TUI!!!!")
            exit()
        else :
            print("Wrong Input")
## CHANGING LOCATION TO REMOTE SYSTEM
    elif location1=='remote':
        if int(ch)==1 :
            os.system("ssh {0} date".format(IP))
        elif int(ch)==2 :
            os.system("ssh {0} cal".format(IP))
        elif int(ch)==3:
            print("Configuring the web Server!!!")
            os.system("ssh {0} yum install httpd".format(IP))
            print("Starting the Web Server!!!")
            os.system("ssh {0} systemctl start httpd".format(IP))
            disFirewall=input("To diasble FIREWALL press Y else N =  ")
            disFirewall2=disFirewall.lower()
            if disFirewall2=='y':
                os.system("ssh {0} systemctl stop firewalld".format(IP))
                print("FIREWALL Disabled !!!!")
            print("Server Started at port 80...")
        elif int(ch)==4:
            print("Enter your user name = ",end="")
            userName=input()
            os.system("ssh {0} useradd {1}".format(IP , userName))
            print("User created!!")
        elif int(ch)==5:
            os.chdir('ssh {} /root'.format(IP))
            os.system("ssh {} ls".format(IP))
            location=input("choose Location = ")
            os.chdir('ssh {} {}'.format(IP,location))
            os.system("ls")
            print("What is your Directory name = ",end="")
            name=input()
            os.system("ssh {0} mkdir {1}".format(IP , name))
            print("Directory Created")
        elif int(ch)==6:
            print("Enter your file name = ",end="")
            FileName=input()
            print("")
            os.system("ssh {0} touch {1}".format(IP, FileName))
            print("File Created")
        elif int(ch)==7:
            os.system("ssh {0} ls".format(IP))
            print("Enter the directory name to Delete = ",end="")
            fileDel=input()
            os.system("ssh {0} rm -r {1}".format(IP , fileDel))
            print("Dir Deleted")
        elif int(ch)==9:
            print("Stoping the Web Server!!")
            os.system("ssh {0} systemctl stop httpd".format(IP))
            print("Web Server STOPED !!!")
        elif int(ch)==10:
            print('Starting Docker')
            os.system('ssh {0} systemctl start docker'.format(IP))
            os.system('ssh {0} docker images'.format(IP))
            imageSel=input("Enter the Image do you want to run = ")
            os.system('ssh {} docker run  -i {}'.format(IP, imageSel))
        elif int(ch)==12:
            print("Exiting the TUI !!!!!")
            exit()
        else :
            print("Wrong Input")
    else :
        print("Location Does'nt exist ")
    
repeat=''
