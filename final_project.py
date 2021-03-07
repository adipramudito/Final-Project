def menu():
    print("\n ---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Kirim email blast")
    print("4. Keluar")

import smtplib, ssl
import getpass
from email.mime.text import MIMEText

x=0
while x!=4:
    menu()
    x=0    
    x=int(input("\nPilihan anda: "))
    if x==1:
        try:
            kontak=open("all_kontak.txt", "r")
            print(kontak.read())
        except:
            print("XXX BELUM ADA KONTAK XXX")
    elif x==2:
        kontak=open("all_kontak.txt","a")
        #nama=input("Nama: ")
        email=input("Email: ")
        #mail_list[nama]=email
        #kontak.write(nama)
        #kontak.write(" ")
        kontak.write(email)
        kontak.write("\n")
        kontak.close()
        print("\n+++ KONTAK BERHASIL DITAMBAH +++")     
    elif x==3:
        try:
            kontak=open("all_kontak.txt","r")
        except:
            print("XXX BELUM ADA KONTAK XXX")
        else:
            port = 0  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = input("Your email: ")  # Enter your address
            password = getpass.getpass(prompt="Type your password and press enter: ")
            subject=input("Email subject: ")
            text=input("Message: ")
            recipients=open("all_kontak.txt","r")
            send_all=recipients.readlines()
            message = MIMEText(text)
            message["Subject"]=subject
            recipients.close()
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, send_all, message.as_string(text))
            print("Email telah berhasil dikirimkan!")
    elif x<0 or x>6:
        print("xxx Pilihan tidak sesuai xxx")
    else:
        print("\n=== TERIMA KASIH===\n")
        x==4

