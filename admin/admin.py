from datetime import datetime
from tkinter import *
import tkinter 
import os
from tkinter import messagebox
import smtplib
from multiprocessing import Process,Value
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time, threading 

from ftplib import FTP
import serverF

p=''
ss = Value('i',0 )
uploading = Value('i',0)
uploaded = Value('i',0)
#Set Tk. ======================================== 
root = tkinter.Tk()
root.geometry("1350x750+0+0")
root.title("ADMIN")
root.configure(bg='dark slate gray')


#Set Tk. ======================================== 

Tops = Label(root,font=('TH Sarabun New',35,'bold'),text="Admin",relief=GROOVE,bd=10,anchor='n',fg="gold", bg="#13293d")
#Tops.pack(side=TOP)
Tops.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.1, anchor='n')


fMainB = Frame(root,width= 1600,height = 2000, bd=8, relief="raise", bg="#13293d")
fMainB.place(x=675, y=73, width=1350, height=600, anchor='n')


# TITLE STORE
fTL = Label(fMainB,font=('TH Sarabun New',25,'bold'),text="Shop",relief=GROOVE,bd=5,anchor='n',fg="white" , bg="#708090")
fTL.place(relx=0.30, rely=0.01, relwidth=0.6, relheight=0.09, anchor='n')

# MAIN STORE
fMLT = Listbox(fMainB,width= 1000,height = 600, bd=2, relief="raise")
fMLT.place(relx=0.3, rely=0.16, relwidth=0.6, relheight=0.83, anchor='n')

# TITLE PARK
fTR = Label(fMainB,font=('TH Sarabun New',25,'bold'),text="Parking",relief=GROOVE,bd=5,anchor='n',fg="white", bg="#708090")
fTR.place(relx=0.8, rely=0.01, relwidth=0.39, relheight=0.09, anchor='n')

# MAIN PARK
fMLR = Listbox(fMainB,width= 500,height = 600, bd=2, relief="raise")
fMLR.place(relx=0.8, rely=0.16, relwidth=0.39, relheight=0.83, anchor='n')

# Collumn PARK
lbr1 = Label(fMainB,font=('TH Sarabun New',10,'bold'),text="Car registration",relief=GROOVE,anchor='n',fg="white",bd=3, bg="black")
lbr1.place(relx=0.709, rely=0.115, relwidth=0.21, relheight=0.045, anchor='n')
lbr2 = Label(fMainB,font=('TH Sarabun New',10,'bold'),text="Date and time",relief=GROOVE,anchor='n',fg="white",bd=3, bg="black")
lbr2.place(relx=0.9, rely=0.115, relwidth=0.19, relheight=0.045, anchor='n')
  

# Collumn store
lbl1 = Label(fMainB,font=('TH Sarabun New',10,'bold'),text="Car registration",relief=GROOVE,anchor='n',fg="white",bd=3, bg="black")
lbl1.place(relx=0.075, rely=0.115, relwidth=0.15, relheight=0.045, anchor='n')
lbl2 = Label(fMainB,font=('TH Sarabun New',10,'bold'),text="Shop",relief=GROOVE,anchor='n',fg="white",bd=3, bg="black")
lbl2.place(relx=0.225, rely=0.115, relwidth=0.15, relheight=0.045, anchor='n')
lbl3 = Label(fMainB,font=('TH Sarabun New',10,'bold'),text="Total",relief=GROOVE,anchor='n',fg="white",bd=3, bg="black")
lbl3.place(relx=0.375, rely=0.115, relwidth=0.15, relheight=0.045, anchor='n')
lbl4 = Label(fMainB,font=('TH Sarabun New',10,'bold'),text="Date and time",relief=GROOVE,anchor='n',fg="white",bd=3, bg="black")
lbl4.place(relx=0.525, rely=0.115, relwidth=0.15, relheight=0.045, anchor='n')








# contrap update
ft = Label(root,font=('TH Sarabun New',40,'bold'),relief=GROOVE,bd=10,anchor='n',fg="black", bg="#13293d")
ft.place(relx=0.9, rely=0, relwidth=0.2, relheight=0.1, anchor='n')

contrab = Label(font=('TH Sarabun New',10,'bold'),bg='dark slate gray',fg="red3",text="SERVER:OFFLINE")                             
contrab.place(relx=0.9, rely=0.025, relwidth=0.1, relheight=0.03, anchor='n' )    
    

#Clock ======================================== 
lb_clock = Label(font='times 16',bg="#13293d",fg="white")
lb_clock.place(relx=0.9, rely=0.055, relwidth=0.07, relheight=0.03, anchor='n' )


def tick():
    global curtime
    curtime = datetime.now().time()
    ftime = curtime.strftime('%H:%M:%S')
    lb_clock.config(text=ftime)
    lb_clock.after(100, tick)

tick()
#Clock ========================================

# ===============================================================  EMAIL   ===============================================================
def mail():
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
    msg['From'] = "thanaphoom.os@gmail.com"
    msg['To'] = "phoomphoomos@gmail.com"
    msg['Subject'] = "ยอดวันที่ " + str(day) +"/"+str(month)+"/"+str(year)
    email_message = "ยอดวันที่ " + str(day) +"/"+str(month)+"/"+str(year)

    input = open("Receipt.txt" , 'r' , encoding="utf-8")
    for line in input:
        email_message = email_message+line
        
    print(email_message)

    body = email_message
    msg.attach(MIMEText(body, 'plain'))
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msg.attach(part)
    text = msg.as_string()

    try:
        input = open("account.txt")
        for line in input:
            ac, pas, re = line.split()
        input.close()
        try:
            # server = smtplib.SMTP('nontri.ku.ac.th', 25)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            try:
                server.login(ac, pas)
                server.sendmail(ac, re, text)
                pop.clearReceipt()
                print("Successfully")
            except:
                print("Incorrect")
            finally:
                print("Quit Server")
                server.quit()
        except :
            print("server not found")
    except e:
        print("file not found",e)

# ===============================================================  End Email   ===============================================================


# ===============================================================  Edit Dialog   ===============================================================
class popupWindow(object):
    def __init__(self,master,Type,data):
        top=self.top=Toplevel(master)
        self.top.geometry("260x260+650+250")
        self.l=Label(top,text="แก้ไขข้อมูล")
        self.l.pack()
        self.type = Type

        if(self.type == 'park'):
            self.l2=Label(top,text="ทะเบียนรถ")
            self.l2.pack()
            self.e=Entry(top)
            self.e.insert(END, data[0])
            self.e.pack()
            self.l3=Label(top,text="เวลา")
            self.l3.pack()
            self.e2=Entry(top)
            self.e2.insert(END, data[1])
            self.e2.pack()

        else:
            self.l2=Label(top,text="ทะเบียนรถ")
            self.l2.pack()
            self.e=Entry(top)
            self.e.insert(END, data[0])
            self.e.pack()
            self.l3=Label(top,text="ร้านค้า")
            self.l3.pack()
            self.e2=Entry(top)
            self.e2.insert(END, data[1])
            self.e2.pack()
            self.l4=Label(top,text="ราคา")
            self.l4.pack()
            self.e3=Entry(top)
            self.e3.insert(END, data[2])
            self.e3.pack()
            self.l5=Label(top,text="เวลา")
            self.l5.pack()
            self.e4=Entry(top)
            self.e4.insert(END, data[3])
            self.e4.pack()
        self.b=Button(top,text='ตกลง',command=self.success,bg="sea green",width=10)
        self.b.pack(pady=10)
        self.b=Button(top,text='ยกเลิก',command=self.unSuccess,bg="firebrick",width=10)
        self.b.pack()
        self.top.resizable(width=False, height=False)
    def success(self):
        if(self.type == 'park'):
            self.value=(self.e.get(),self.e2.get())
        else:
            self.value = (self.e.get(),self.e2.get(),self.e3.get(),self.e4.get())
        self.top.destroy()
    def unSuccess(self):
        self.value = (False)
        self.top.destroy()

# ===============================================================  End Edit Dialog   ===============================================================

# ===============================================================  SERVER   ====================================================================

            

# ===============================================================  END SERVER   ====================================================================
parkList = []
storeList  = []
recieptList = [] 
# ===============================================================  RENDER HANDLER   ===============================================================
def readFile():
    global parkList , storeList ,recieptList
    parkFile = open("Park.txt" , "r",encoding="utf-8")
    parkList = []

    for i in parkFile:
        carAndTime = i.strip().split(";")
        if(len(carAndTime[0])>8):
            parkList.append(carAndTime)

    parkFile.close()
    storeFile = open("Store.txt","r",encoding="utf-8")
    storeList = []
    for i in storeFile:
        storeDetail = i.strip().split(";")
        if(len(storeDetail[0])>8):
            storeList.append(storeDetail)
    storeFile.close()

def sendUpdate (arr,types):
    uploading.value = 1
    out = open("Output.txt","w",encoding="utf-8")
    if(types == 'Park'):
        # print('update Park')
        out.write('ทะเบียน;เวลา\n')
        for i in arr :
            a = (i[0])+';'+(i[1])
            out.write(a+'\n')
        out.write('ทะเบียน;เวลา\n')
        out.close()
        pop.uploadFile('Park.txt')
        
    else:
        out.write('ทะเบียน;ชื่อร้าน;ราคา;เวลา\n')
        for i in arr :
            out.write((i[0])+';'+(i[1])+';'+(i[2])+';'+(i[3])+'\n')
        out.close()
        pop.uploadFile('Store.txt') 
    
def tranferStore(T):
    T=str(T)
    Stext=len(T)
    space=(56-Stext)
    t=T
    l = 0
    r = 0
    for p in range(space):
        if(p%2==0):
            t=" "+t
            l=l+1
        else:
            t= t+" "
            r=r+1
    return t  

def tranferPark(T):
    T=str(T)
    Stext=len(T)
    space=(74-Stext)
    t=T
    for p in range(space):
        if(p%2==0):
            t=" "+t
        else:
            t= t+" "
    return t  

def render (Type) :
    if(Type =='park'):
        fMLR.delete(0,len(parkList))
        for i in range (len(parkList)):
            strr = (tranferPark(parkList[i][0])+tranferPark(parkList[i][1]))
            print("strr = ",strr)
            fMLR.insert(END,strr)
    elif(Type == 'store'):
        fMLT.delete(0,len(storeList))
        for i in range (len(storeList)):
            fMLT.insert(END,tranferStore(storeList[i][0])+tranferStore(storeList[i][1])+tranferStore(storeList[i][2])+tranferStore(storeList[i][3]))
    else:
        fMLR.delete(0,len(parkList))
        for i in range (len(parkList)):
            fMLR.insert(END,tranferPark(parkList[i][0])+tranferPark(parkList[i][1]))

        fMLT.delete(0,len(storeList))
        for i in range (len(storeList)):
            strr = tranferStore(storeList[i][0])+tranferStore(storeList[i][1])+tranferStore(storeList[i][2])+tranferStore(storeList[i][3])
            fMLT.insert(END,strr)


     
def update():
    print('StartFrontUpdate!')
    if(uploaded.value == 1):
        uploaded.value = 0
        if(ss.value == 1):
            contrab['text'] = 'SERVER:ONLINE'
            contrab['fg'] = 'cyan3'
        else :
            contrab['text'] = 'SERVER:OFFLINE'
            contrab['fg'] = 'red3'
        if(uploading.value == 0 and ss.value == 1):
            readFile()
            render('both') 

    t1  = threading.Timer(8, update,)
    t1.setDaemon(TRUE)
    t1.start()



# ===============================================================  END RENDER HANDLER   ===============================================================

# ===============================================================  Button   ===============================================================
def editItem():
    # fMLR.curselection() != () that mean we're selected at the  parkList 
    if(fMLR.curselection()):
        # can check here 
        # print('check park = ')
        # print(fMLR.curselection())
        # print('check store = ')
        # print(fMLT.curselection())
        index = fMLR.curselection()
        i = index[0]
        w= popupWindow(root,'park', [parkList[i][0],parkList[i][1]])
        root.wait_window(w.top)
        if(w.value):
            car,time = w.value
            parkList[i][0] = car
            parkList[i][1] = time
            render('park')
            sendUpdate (parkList,'Park')
    elif (fMLT.curselection()):
        # print('check storeList : ',storeList)
        index = fMLT.curselection()
        i = index[0]
        
        w= popupWindow( root,'store',[storeList[i][0],storeList[i][1],storeList[i][2],storeList[i][3]] )
        root.wait_window(w.top)
        if(w.value):
            car,store,price,time = w.value
            storeList[i][0] = str(car)
            storeList[i][1] = str(store)
            storeList[i][2] = str(price)
            storeList[i][3] = str(time)
            render('store')
            sendUpdate (storeList,'Store')
    else :
        tkinter.messagebox.showwarning(title=Warning, message='กรุณาเลือกข้อมูลก่อน')


def deleteItem():
    # same reason at editItem
    if(fMLR.curselection()):
        index = fMLR.curselection()
        i = index[0]
        answer = messagebox.askyesno("ยืนยันการลบ", "ยืนยันที่จะลบหรือไม่\n"+parkList[i][0]+" "+parkList[i][1])
        if(answer):
            parkList.pop(i)
            # fMLR.delete(fMLR.curselection())
            ###### i got bug when use .delete then i decied to use render  ######
            sendUpdate (parkList,'Park')
            render('park')
            
    elif(fMLT.curselection()):
        index = fMLT.curselection()
        i = index[0]
        answer = messagebox.askyesno("ยืนยันการลบ", "ยืนยันที่จะลบหรือไม่\n"+storeList[i][0]+" "+storeList[i][1]+" "+storeList[i][2]+" "+storeList[i][3])
        if(answer):
            storeList.pop(i)
            # fMLT.delete(fMLR.curselection())
            sendUpdate (storeList,'Store')
            render('store')
    else :
        tkinter.messagebox.showwarning(title=Warning, message='กรุณาเลือกข้อมูลก่อน')        
# ===============================================================  //Button   ===============================================================


# ================================================= email ===============================================================
class previewFile(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.top.geometry("600x250+500+300")
        self.l=Label(top,text="ข้อมูลในไฟล์ก่อนส่ง")
        self.l.pack()

        self.e3 = Listbox(top , width = 80)
        self.e3.pack()
        input = open("Receipt.txt" , 'r' , encoding="utf-8")
        for line in input:
            print(line)
            self.e3.insert(END ,line)
        input.close()
        self.b=Button(top,text='ส่งอีเมลล์',command=self.success,bd=5,bg="sea green",fg="white",width=10)
        self.b.place(relx=0.4, rely=0.80, relwidth=0.20, relheight=0.15, anchor='n')
        self.b=Button(top,text='ยกเลิก',command=self.unSuccess,bd=5,bg="firebrick",fg="white",width=10)
        self.b.place(relx=0.6, rely=0.80, relwidth=0.20, relheight=0.15, anchor='n')
        self.top.resizable(width=False, height=False)


    def success(self):
        #send mail
        #eiei
        mail()

        # if(self.type == 'park'):
        #     self.value=(self.e.get(),self.e2.get())
        # else:
        #     self.value = (self.e.get(),self.e2.get(),self.e3.get(),self.e4.get())
        self.top.destroy()
    def unSuccess(self):
        self.value = (False)
        self.top.destroy()
    

def finish():
    #eiei
    w= previewFile(root)
    root.wait_window(w.top)


# ================================================= //email =======================================
###### edit button #########
fbb = Frame(root,width= 1600,height = 2000, bd=8, relief="raise", bg="#13293d")
fbb.place(x=675, y=675, width=1350, height=74, anchor='n')

button = tkinter.Button(fbb,font=('TH Sarabun New',14,'bold'), text="Edit selected data", command=editItem,bd=5,bg="sea green",fg="white")
button.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.8, anchor='n')
            
######delete button #########
button = tkinter.Button(fbb,font=('TH Sarabun New',14,'bold'), text="Delete selected data", command=deleteItem,bg="firebrick",fg="white")
button.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.8, anchor='n')



########dialog Finish

fb = Label(root,font=('TH Sarabun New',40,'bold'),relief=GROOVE,bd=10,anchor='n',fg="black", bg="#13293d")
#Tops.pack(side=TOP)
fb.place(relx=0.1, rely=0, relwidth=0.2, relheight=0.1, anchor='n')

button=Button(fb,fg="white",font=('TH Sarabun New',14,'bold'),width=5,text="Balance report",command=finish,bg="firebrick")
button.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.8, anchor='n')





if __name__ == '__main__':
    # *************************************** MAIN ***************************************
    pop = serverF.Pop(ss,uploading,uploaded)
    pop.daemon = True
    pop.start()

    update()
    root.resizable(width=False, height=False)
    root.mainloop()
