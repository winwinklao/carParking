from ftplib import FTP
from datetime import datetime
from tkinter import *
import tkinter
from tkinter import messagebox
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

root = tkinter.Tk()
root.geometry("1350x750+0+0")
root.title("CAR PARKING")
root.configure(bg='#13293d')

regis1 = StringVar()
regis2 = StringVar()
intime1 = StringVar()
outtime1 = StringVar()
totaltime = StringVar()
total = StringVar()
receivemoney = StringVar(root, "0")
change = StringVar(root, "0")

# ***************************************time*********************************************
now = datetime.now()
timestamp = datetime.timestamp(now)
time = datetime.fromtimestamp(timestamp)
time = str(time)
day = int(time[8] + time[9])
month = int(time[5] + time[6])
year = int(time[0] + time[1] + time[2] + time[3])
hour = int(time[11] + time[12])
minute = int(time[14] + time[15])

# ************************************OPTION*************************************************

def Reset():
    regis2.set("")
    intime1.set("")
    outtime1.set("")
    totaltime.set("")
    total.set("")
    receivemoney.set("0")
    change.set("0")
    btnCon.config(state=tkinter.DISABLED)

def qExit():
    root.destroy()

def dowloadFile(filename):
    try:
        input = open("login.txt")
        for line in input:
            in1, in2, in3, in4 = line.split()
        input.close()
        ftp = FTP(in1)
        ftp.login(user=in2, passwd=in3)
    except:
        print("Login Dowload EROR")

    ftp.cwd('Assigngroup1')
    try:
        localfile = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
        localfile.close()
        ftp.quit()
    except:
        ftp.quit()
        for i in range(100000):
            if i % 1000 == 0:
                print("Press wait....")
        dowloadFile(filename)


def uploadFile(filename):
    try:
        input = open("login.txt")
        for line in input:
            in1, in2, in3, in4 = line.split()
        input.close()
        ftp = FTP(in1)
        ftp.login(user=in2, passwd=in3)
    except:
        print("Login Upload EROR Please Check VPN")
        return 0
    ftp.cwd('Assigngroup1')
    try:
        ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
        ftp.quit()
    except:
        ftp.quit()
        for i in range(100000):
            if i % 1000 == 0:
                print("Press wait....")
        uploadFile(filename)


def addcar():
    regis = str(regis1.get())
    if regis != '':
        try:
            dowloadFile('Park.txt')
        except:
            print("dowload ERROR")
        try:
            input = open("Park.txt", encoding="utf-8")
            for line in input:
                in1, in2 = line.split(';')
                if in1 == regis:
                    messagebox.showwarning(title="Warning", message="Available Car")
                    return 0
            input.close()
        except:
            print("Check Park Error")
        try:
            input = open("login.txt")
            for line in input:
                in1, in2, in3, in4 = line.split()
            input.close()
            ftp = FTP(in1)
            ftp.login(user=in2, passwd=in3)
        except:
            print("Add Error Please Check VPN")
            return 0

        ftp.cwd('Assigngroup1')
        ftp.delete('Park.txt')
        ftp.quit()
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        time = datetime.fromtimestamp(timestamp)
        time = str(time)
        try:
            save = []
            input = open("Park.txt", encoding="utf-8")
            for line in input:
                in1, in2 = line.split(';')
                if in1 != 'ทะเบียน':
                    save.append(line)
            input.close()

            os.remove("Park.txt")
            name = open("Park.txt", "w", encoding="utf-8")
            name.write("ทะเบียน;เวลา")
            name.write("\n")
            for i in save:
                name.write(i)
            name.close()

            with open("Park.txt", "a", encoding="utf-8") as input:
                word = regis + ';' + time
                input.write(word)
                input.write("\n")
                input.write("ทะเบียน;เวลา")

            regis1.set("")
            print("Write park ->", word)
            try:
                uploadFile("Park.txt")
            except:
                print("Upload park ERROR")
        except:
            for i in range(100000):
                a = 0
            addcar()


def calculate():
    try:
        dowloadFile('Park.txt')
        dowloadFile('Receipt.txt')
        dowloadFile('Store.txt')
    except:
        print("dowload ERROR")
        return 0
    try:
        if regis2.get() != "":
            register = regis2.get()
            amount = 0
            payment = 0

            now = datetime.now()
            timestamp = datetime.timestamp(now)
            time = datetime.fromtimestamp(timestamp)
            time = str(time)

            day = int(time[8] + time[9])
            month = int(time[5] + time[6])
            year = int(time[0] + time[1] + time[2] + time[3])
            hour = int(time[11] + time[12])
            minute = int(time[14] + time[15])

            input = open("Store.txt", encoding="utf-8")
            for line in input:
                in1, in2, in3, in4 = line.split(';')
                if register == in1:
                    amount = amount + int(float(in3))
            input.close()

            try:
                state=0
                intime = ''
                input = open("Park.txt", encoding="utf-8")
                for line in input:
                    in1, in2 = line.split(';')
                    if register == in1:
                        state=1
                        intime = in2
                input.close()
                if state==0:
                    regis2.set("Not Found")
                    return 0
                dayin = int(intime[8] + intime[9])
                monthin = int(intime[5] + intime[6])
                yearin = int(intime[0] + intime[1] + intime[2] + intime[3])
                hourin = int(intime[11] + intime[12])
                minutein = int(intime[14] + intime[15])

                print("in  ", dayin, monthin, yearin, " ", hourin, ":", minutein)
                print("out ", day, month, year, " ", hour, ":", minute)

                if day != dayin:
                    hours = (24 - hourin) + hour
                else:
                    hours = hour - hourin
                if hour != hourin:
                    if minutein == 0:
                        minutes = minute
                    else:
                        if minute>minutein:
                            minutes = minute - minutein
                        else:
                            hours=hours-1
                            minutes = (60 - minutein) + minute
                else:
                    minutes = minute - minutein
                    # print(hours)
                    # print(minutes)
                    # if minutes >= 60:
                    #     minutes = minutes - 60
                    #     hours = hours + 1
                print("time -> ", hours, ":", minutes)


                if 100 <= amount and amount < 1000 and hours!=0:
                    hours = hours - 1

                payment = payment + (hours) * 30

                if minutes > 30 and hours!=0:
                    payment = payment + 30
                if amount >= 1000 and hours <= 24:
                    payment = 0

                if year > yearin:
                    payment = (year - yearin + 1) * 120000
                if month > monthin:
                    payment = (month - monthin + 1) * 30000
                if abs(day - dayin) > 1:
                    payment = (day - dayin + 1) * 1000
                if intime == '':
                    regis2.set("Not Found")
                    return 0
                print("Payment = ", payment)
                s1 = str(dayin) + "/" + str(monthin) + "/" + str(yearin) + " " + str(hourin) + ":" + str(minutein)
                s2 = str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(minute)
                s3 = str(hours) + ":" + str(minutes)
                intime1.set(s1)
                outtime1.set(s2)
            except:
                print("Input Data Error ")
                regis2.set("Data Error")
                return 0

    # if regis2.get() != "":
    #     register = regis2.get()
    #     amount = 0
    #     payment = 0
    #
    #     now = datetime.now()
    #     timestamp = datetime.timestamp(now)
    #     time = datetime.fromtimestamp(timestamp)
    #     time = str(time)
    #
    #     day = int(time[8] + time[9])
    #     month = int(time[5] + time[6])
    #     year = int(time[0] + time[1] + time[2] + time[3])
    #     hour = int(time[11] + time[12])
    #     minute = int(time[14] + time[15])
    #
    #     input = open("Store.txt", encoding="utf-8")
    #     for line in input:
    #         in1, in2, in3, in4 = line.split(';')
    #         if register == in1:
    #             amount = amount + int(float(in3))
    #     input.close()
    #     try:
    #         intime = ''
    #         input = open("Park.txt", encoding="utf-8")
    #         for line in input:
    #             in1, in2 = line.split(';')
    #             if register == in1:
    #                 intime = in2
    #         input.close()
    #
    #         dayin = int(intime[8] + intime[9])
    #         monthin = int(intime[5] + intime[6])
    #         yearin = int(intime[0] + intime[1] + intime[2] + intime[3])
    #         hourin = int(intime[11] + intime[12])
    #         minutein = int(intime[14] + intime[15])
    #
    #         print("in  ", dayin, monthin, yearin, " ", hourin, ":", minutein)
    #         print("out ", day, month, year, " ", hour, ":", minute)
    #
    #         if day != dayin:
    #             hours = (24 - hourin) + hour
    #         else:
    #             hours = hour - hourin
    #         if hour != hourin:
    #             if minutein == 0:
    #                 minutes = minute
    #             else:
    #                 if minute>minutein:
    #                     minutes = minute - minutein
    #                 else:
    #                     hours=hours-1
    #                     minutes = (60 - minutein) + minute
    #         else:
    #             minutes = minute - minutein
    #             # print(hours)
    #             # print(minutes)
    #             # if minutes >= 60:
    #             #     minutes = minutes - 60
    #             #     hours = hours + 1
    #         print("time -> ", hours, ":", minutes)
    #
    #         if 100 <= amount and amount < 1000:
    #             hours = hours - 1
    #
    #         payment = payment + (hours) * 30
    #
    #         if minutes > 30:
    #             payment = payment + 30
    #         if amount >= 1000 and hours <= 24:
    #             payment = 0
    #
    #         if year > yearin:
    #             payment = (year - yearin + 1) * 120000
    #         if month > monthin:
    #             payment = (month - monthin + 1) * 30000
    #         if abs(day - dayin) > 1:
    #             payment = (day - dayin + 1) * 1000
    #         if intime == '':
    #             regis2.set("Not Found")
    #         print("Payment = ", payment)
    #         s1 = str(dayin) + "/" + str(monthin) + "/" + str(yearin) + " " + str(hourin) + ":" + str(minutein)
    #         s2 = str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(minute)
    #         s3 = str(hours) + ":" + str(minutes)
    #         intime1.set(s1)
    #         outtime1.set(s2)
    #     except:
    #         print("Input Data Error ")
    #         regis2.set("Data Error")
    #         return 0

    except:
        print("Calculate Error")
        messagebox.showwarning(title="Warning", message="Please input again")
        return 0

    try:
        agtime = ''
        for i in intime:
            if i != "\n":
                agtime = agtime + i
        if payment <= 1000:
            totaltime.set(s3 + " ชั่วโมง")
            with open("Receipt.txt", "a", encoding="utf-8") as input:
                word = str(register) + ';' + agtime + ';' + str(time) + ';' + str(s3 + " ชั่วโมง") + ';' + str(payment)
                input.write("\n")
                input.write(word)
        else:
            totaltime.set(">24 ชั่วโมง")
            with open("Receipt.txt", "a", encoding="utf-8") as input:
                word = str(register) + ';' + agtime + ';' + str(time) + ";" + str(">24 ชั่วโมง") + ';' + str(payment)
                input.write("\n")
                input.write(word)
        total.set(str(payment))
    except:
        regis2.set("Not Found")
    try:
        dowloadFile('Park.txt')
    except:
        print("dowload ERROR")
    try:
        save = []
        input = open("Park.txt", encoding="utf-8")
        for line in input:
            in1, in2 = line.split(';')
            if regis2.get() != in1 and regis2.get() != '/n':
                save.append(line)
        input.close()
        os.remove("Park.txt")
        name = open("Park.txt", "w", encoding="utf-8")
        for i in save:
            name.write(i)
        name.close()
    except:
        print("Remove Park Error")

def ok():
    try:
        ch1 = int(receivemoney.get())
    except:
        messagebox.showwarning(title="Warning", message="Please input the number for the cash field.")
    else:
        if int(total.get()) != 0:
            if int(receivemoney.get()) < int(total.get()):
                messagebox.showwarning(title="Warning", message="Enough Money!!!!")
                return 0
            receive = int(receivemoney.get()) - int(total.get())
            change.set(str(receive))
            messagebox.showinfo(title="COMPLETE", message="Complete!!!!")
    try:
        uploadFile('Park.txt')
        uploadFile('Receipt.txt')
    except:
        print("Upload receipt ERROR")

    btnCon.config(state=tkinter.NORMAL)

def mail():
    try:
        dowloadFile('Receipt.txt')
    except:
        print("dowload ERROR")
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    time = datetime.fromtimestamp(timestamp)
    time = str(time)
    day = int(time[8] + time[9])
    month = int(time[5] + time[6])
    year = int(time[0] + time[1] + time[2] + time[3])
    hour = int(time[11] + time[12])
    minute = int(time[14] + time[15])

    msg = MIMEMultipart()
    msg['From'] = "rathanonproject@gmail.com"
    msg['To'] = "peemrathanon.ht@gmail.com"
    msg['Subject'] = "ยอดวันที่ " + str(day) + "/" + str(month) + "/" + str(year)
    email_message = "ยอดวันที่ " + str(day) + "/" + str(month) + "/" + str(year)
    body = email_message
    msg.attach(MIMEText(body, 'plain'))
    filename = "Receipt.txt"
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    text = msg.as_string()

    try:
        input = open("account.txt")
        for line in input:
            ac, pas, re = line.split()
        input.close()
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            try:
                server.login(ac, pas)
                server.sendmail(ac, re, text)
                print("Successfully")
            except:
                print("Incorrect")
            finally:
                print("Quit Server")
                server.quit()
                name = open("Receipt.txt", "w", encoding="utf-8")
                name.write("ทะเบียน;เวลาเข้า;เวลาออก;ชั่วโมง;ราคา")
                name.close()
                uploadFile("Receipt.txt")
        except:
            print("server not found")
    except:
        print("file not found")


# ***************************************GUI*****************************************************

# ---------------------setting---------------------
def gui():
    Tops = Label(root, width=1350, font=('times new roman', 40, 'bold'), text="CAR PARKING", relief=GROOVE, fg="gold",
                 bg="#13293d", bd=10)
    Tops.pack(side=TOP)

    # Tops=LabelFrame(root , width= 1350, bg="powder blue", relief=GROOVE, bd=4)
    # Tops.pack(side=TOP)

    f1 = LabelFrame(root, text='Inbound', font=('times new roman', 30, 'bold'), fg="gold", bg="#13293d", bd=6,
                    relief=GROOVE)
    f1.place(x=0, y=84, width=675, height=580)

    f2 = LabelFrame(root, text='Departure', font=('times new roman', 30, 'bold'), fg="gold", bg="#13293d", bd=6,
                    relief=GROOVE)
    f2.place(x=675, y=84, width=675, height=580)


    f3 = LabelFrame(root, relief=GROOVE, fg="gold", bg="#13293d", bd=6)
    f3.place(x=0, y=665, width=1350, height=85)

    fk = LabelFrame(f1, font=('times new roman', 12, 'bold'), bg="#13293d", bd=0)
    fk.place(x=30, y=220, width=600, height=200)

    fb = LabelFrame(f3, font=('times new roman', 12, 'bold'), bg="#13293d", bd=0)
    fb.place(x=500, y=0)

    # ---------------------POS---------------------

    # lblInfo = Label(Tops,font=('TH Sarabun New',50,'bold'), width= 1350, text="CAR PRKING",fg="royal blue",bd=5,anchor='w')
    # lblInfo.grid(row=0,column=0, padx = 50)

    # lblMenu6 =Label(fk, font=('TH Sarabun New',30,'bold'),text="ขาเข้า" ,bd=16 )
    # lblMenu6.grid(row=0,column=1)

    lblMenu1 = Label(f2, font=('TH Sarabun New', 2, 'bold'), bg="#13293d", bd=10)
    lblMenu1.grid(row=0, column=1)

    lblRef = Label(fk, font=('TH Sarabun New', 18, 'bold'), text='Car registration', bd=16, fg="white", bg="#13293d",anchor='e')
    lblRef.grid(row=1, sticky=E)
    textRef = Entry(fk, font=('TH Sarabun New', 18, 'bold'), textvar=regis1, fg="black", bg="powder blue",justify='center')
    textRef.grid(row=1, column=1)

    lblMenu2 = Label(f2, font=('TH Sarabun New', 18, 'bold'), text="Car registration", fg="white", bg="#13293d", bd=16,anchor='e')
    lblMenu2.grid(row=1, sticky=E)
    textMenu2 = Entry(f2, font=('TH Sarabun New', 18, 'bold'), textvar=regis2, fg="black", bg="powder blue",justify='center')
    textMenu2.grid(row=1, column=1)

    lblMenu3 = Label(f2, font=('TH Sarabun New', 18, 'bold'), text="Time in", fg="white", bg="#13293d", bd=16,anchor='e')
    lblMenu3.grid(row=2, sticky=E)
    textMenu3 = Entry(f2, font=('TH Sarabun New', 18, 'bold'), textvar=intime1, fg="orange", bg="light slate gray",justify='center', state='disabled')
    textMenu3.grid(row=2, column=1)

    lblMenu4 = Label(f2, font=('TH Sarabun New', 18, 'bold'), text="Time out", fg="white", bg="#13293d", bd=16,anchor='e')
    lblMenu4.grid(row=3, sticky=E)
    textMenu4 = Entry(f2, font=('TH Sarabun New', 18, 'bold'), textvar=outtime1, fg="orange", bg="light slate gray",justify='center', state='disabled')
    textMenu4.grid(row=3, column=1)

    lblMenu5 = Label(f2, font=('TH Sarabun New', 18, 'bold'), text="Total parking time", fg="white", bg="#13293d",bd=16, anchor='e')
    lblMenu5.grid(row=4, sticky=E)
    textMenu5 = Entry(f2, font=('TH Sarabun New', 18, 'bold'), textvar=totaltime, fg="orange", bg="light slate gray",justify='center', state='disabled')
    textMenu5.grid(row=4, column=1)

    lblMenu6 = Label(f2, font=('TH Sarabun New', 18, 'bold'), text="Charge amount", fg="white", bg="#13293d", bd=16,anchor='e')
    lblMenu6.grid(row=5, sticky=E)
    textMenu6 = Entry(f2, font=('TH Sarabun New', 18, 'bold'), textvar=total, fg="orange", bg="light slate gray",justify='center', state='disabled')
    textMenu6.grid(row=5, column=1)

    lblMenu7 = Label(f2, font=('TH Sarabun New', 18, 'bold'), text="Cash", fg="white", bg="#13293d", bd=16, anchor='e')
    lblMenu7.grid(row=7, sticky=E)
    textMenu7 = Entry(f2, font=('TH Sarabun New', 18, 'bold'), textvar=receivemoney, bg="powder blue", justify='center')
    textMenu7.grid(row=7, column=1)

    lblMenu8 = Label(f2, font=('TH Sarabun New', 18, 'bold'), text="Change", fg="white", bg="#13293d", bd=16,anchor='e')
    lblMenu8.grid(row=8, sticky=E)
    textMenu8 = Entry(f2, font=('TH Sarabun New', 18, 'bold'), textvar=change, fg="orange", bg="light slate gray",justify='center', state='disabled')
    textMenu8.grid(row=8, column=1)

    btnTotal = Button(fk, bd=5, fg="black", font=('TH Sarabun New', 14, 'bold'), width=6, text="Submit",bg="powder blue", command=addcar)
    btnTotal.grid(row=1, column=2, padx=10)

    btnCal = Button(f2, bd=5, fg="black", font=('TH Sarabun New', 14, 'bold'), width=8, text="Calculate",bg="powder blue", command=calculate)
    btnCal.grid(row=1, column=3, padx=20)

    btnSub = Button(f2, bd=5, fg="black", font=('TH Sarabun New', 14, 'bold'), width=6, text="Submit",bg="powder blue", command=ok)
    btnSub.grid(row=7, column=3, padx=10)

    global btnCon
    btnCon = Button(f2, bd=5, fg="black", font=('TH Sarabun New', 14, 'bold'), width=6, text="Confirm",bg="powder blue", command=Reset, state=DISABLED)
    btnCon.grid(row=8, column=3)

    # btnExit = Button(fb, fg="black", font=('TH Sarabun New', 18, 'bold'), width=12, text="Balance report", bg="gold",
    #                  command=mail)
    # btnExit.grid(row=0, column=0)

    btnExit = Button(fb, bd=5 , fg="black", font=('TH Sarabun New', 18, 'bold'), width=6, text="Exit", bg="red", command=qExit)
    btnExit.grid(row=0, column=3, padx=700, pady=10)

    root.mainloop()

try:
    dowloadFile('Park.txt')
    dowloadFile('Receipt.txt')
    dowloadFile('Store.txt')
except:
    print('Dowload First Error')

try:
    gui()
except:
    gui()
# ***********************************************************************************************


