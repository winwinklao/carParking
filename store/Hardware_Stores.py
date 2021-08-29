from tkinter import *
from tkinter import messagebox
from ftplib import FTP
import random
import time
import os
from datetime import datetime

        
try:
    ip = open("login.txt")
except IOError:
    print("Error : can't find file or read data")
else:
    for i in ip:
        FTPServer, Username, Password= i.split(';')
        try:
            ftp = FTP(FTPServer)
            ftp.login(user=Username, passwd=Password)
            ftp.cwd('Assigngroup1')
        except:
            print("Can not Login!!!\n")
            print("Please try again :)")
            break
        
        def downloadFile(filename):
            try:
               
                localfile = open(filename, 'wb')
                ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
                localfile.close()
            except:
                print("Can not downlload file!!!")
                    
            
        def uploadFile(filename):
            try:
                ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
            except:
                print("Can not upload file!!!")
        try:
            ipShop = open("NamePOS.txt")
        except IOError:
            print("Error : can't find file or read data")
                    
        else:
            for i in ipShop:
                NameShop, MenuType1, MenuType2, Type1, Type2, Service, tax= i.split(';')
                filenameInput = 'Store.txt'
                downloadFile(filenameInput)
                root = Tk()
                root.geometry("1350x750+0+0")
                root.title(NameShop)
                root.configure(background='pink')
                
                dateTimeObj = datetime.now()
                
                #============================ Frame ========================================
                
                Tops = Label(root, width= 1350, font=('times new roman', 40, 'bold'), text = NameShop, relief=GROOVE,fg="gold", bg="#332222", bd=10)
                Tops.pack(side=TOP) 
                
                fCarRigis = LabelFrame(root, text='Customer Details', font=('times new roman', 12, 'bold'),fg="gold",  width= 1350, height = 6, relief=GROOVE, bg="#392214", bd=10)
                fCarRigis.pack(fill=X)
                
                fMainL = Label(root,width= 900,height = 650, bd=10, relief=GROOVE)
                fMainL.pack(side=LEFT)
                
                fMainR = Label(root,width= 440,height = 650, bd=10, relief=GROOVE)
                fMainR.pack(side=RIGHT)
                
                fMenu1 = LabelFrame(root, text='Menu '+ MenuType1, font=('times new roman', 12, 'bold'),fg="gold", bd=10, bg="#775533", relief=GROOVE)
                fMenu1.place(x=0, y=180, width=490, height=400)
                fMenu2 = LabelFrame(root, text='Menu '+ MenuType2, font=('times new roman', 12, 'bold'),fg="gold" ,bd=10, bg="#775533", relief=GROOVE)
                fMenu2.place(x=490, y=180, width=490, height=400)
                
                fReceipt = LabelFrame(root, text='Receipt', font=('times new roman', 12, 'bold'),fg="gold",  bd=10, bg="#392214", relief=GROOVE)
                fReceipt.place(x=980, y=180, width=370, height=400)
                
                fCost1 = LabelFrame(root, text='Receipt Menu', font=('times new roman', 12, 'bold'),bg="#392214", fg="gold",width= 490,height = 330, bd=10, relief=GROOVE)
                fCost1.place(x=0, y=580, width=980, height=170)
                fButton = LabelFrame(root,width= 490,height = 320, bd=10,bg="#392214",relief=GROOVE)
                fButton.place(x=980, y=580, width=370, height=170)
                
                
                #============================Read Flie========================
                Menu1List = []
                Menu2List = []
                ProductPriceList = []
                GoodsPriceList = []
                try:
                    ipC = open("coffee.txt")
                    
                except IOError:
                    print("Error : can't find file or read data")
                else:
                    for i in ipC:
                        nameC, p = i.split('=')
                        Menu1List.append(nameC)
                        ProductPriceList.append(int(p))
                    ipC.close()
                
                try:
                    ipCa = open("cake.txt")
                    
                except IOError:
                    print("Error : can't find file or read data")
                else:
                    for i in ipCa:
                        nameCa, p = i.split('=')
                        Menu2List.append(nameCa)
                        GoodsPriceList.append(int(p))
                    ipCa.close()
                
                
                    
                #============================= Function =====================
                def qExit():
                    qExit= messagebox.askyesno("Quit System!!!", "Do you want to quit?")
                    if qExit > 0:
                        root.destroy()
                        return
                def Reset():
                    FrameProductReset()
                    FrameGoodsReset()
                    FrameCostReset()
                    txtReceipt.delete("1.0",END)
                
                def FrameProductReset():
                            
                    for i in VarProductList:    
                        i.set("0")
                
                    for i in EntryProductList:    
                        i.set("0")
                
                    txtProduct0.configure(state = DISABLED)
                    txtProduct1.configure(state = DISABLED)
                    txtProduct2.configure(state = DISABLED)
                    txtProduct3.configure(state = DISABLED)
                    txtProduct4.configure(state = DISABLED)
                    txtProduct5.configure(state = DISABLED)
                    txtProduct6.configure(state = DISABLED)
                    txtProduct7.configure(state = DISABLED)
                def FrameGoodsReset():
                    for x in VarGoodsList:    
                        x.set("0")
                
                    for x in EntryGoodsList:    
                        x.set("0")
                
                    txtGoods0.configure(state = DISABLED)
                    txtGoods1.configure(state = DISABLED)
                    txtGoods2.configure(state = DISABLED)
                    txtGoods3.configure(state = DISABLED)
                    txtGoods4.configure(state = DISABLED)
                    txtGoods5.configure(state = DISABLED)
                    txtGoods6.configure(state = DISABLED)
                    txtGoods7.configure(state = DISABLED)
                    
                def FrameCostReset():
                    CostofProduct.set("")
                    CostofGoods.set("")
                    ServiceCharge.set("")
                    PaidTax.set("")
                    SubTotal.set("")
                    TotalCost.set("")
                    CostofProduct.set("")
                    CostofGoods.set("")
                    CarRigis.set("")
                                 
                def chkbutton_value(chkValue,txtLabel,Entry):
                    if chkValue.get() == 1:
                        txtLabel.configure(state=NORMAL)
                    elif chkValue.get() == 0:
                        txtLabel.configure(state=DISABLED)
                        Entry.set("0")
                
                def CostofItem():    
                    TotalProductCost = 0
                       
                    TotalGoodsCost = 0
                       
                    for i in range(8) :
                        try:  
                            ep = int(EntryProductList[i].get())
                            eg = int(EntryGoodsList[i].get())
                            pp = float(ProductPriceList[i])
                            gp = float(GoodsPriceList[i])
                        except ValueError:
                            messagebox.showwarning(title="Warning", message="Please input the number for the menu field.")
                        else:
                            TotalProductCost += int(ep)* float(pp)
                            TotalGoodsCost += int(eg)* float(gp)
                
                    ProductPrice = "B", str('%.2f'%(TotalProductCost))
                    GoodsPrice = "B", str('%.2f'%(TotalGoodsCost))
                    CostofProduct.set(ProductPrice)
                    CostofGoods.set(GoodsPrice)
                    SC = "B", str('%.2f'%(float(Service)))
                    ServiceCharge.set(SC)
                
                    CostPlus = TotalProductCost + TotalGoodsCost + float(Service)
                        
                    SubTotalofItems = "B", str('%.2f'%(CostPlus))
                    SubTotal.set(SubTotalofItems)
                
                    Tax = "B" , str('%.2f'%(CostPlus*float(tax)))
                    PaidTax.set(Tax)
                    TT = CostPlus * float(tax)
                    TC = str('%.2f'%(CostPlus + TT))
                    TotalCost.set(TC)
            
                
                def Receipt():
                    li = []
                    filenameInput = 'Store.txt'
                    downloadFile(filenameInput)
                    filenamePark = 'Park.txt'
                    downloadFile(filenamePark)
                    try:
                        dd = open("Park.txt", encoding="utf-8")
                    except IOError:
                        print("Error : can't find file or read data")
                        return 0
                    else:
                        print("Written content in the file successfully")
                        for line in dd:
                            rigis, tt = line.split(';')
                            li.append(rigis)
                        dd.close()
                    if(CarRigis.get() == ""):
                        messagebox.showwarning(title="Warning", message="Please input  car registration!!!")
                    else:
                        txtReceipt.delete("1.0",END)
                        x = random.randint(10908,500876)
                        randomRef = str(x)
                        ReceiptRef.set("BILL"+ randomRef)
                        ch = 0
                        
                        txtReceipt.insert(END,'Receipt Ref:\t\t'+ ReceiptRef.get()  + '\t\t' + DateofOrder.get() + "\n")
                        txtReceipt.insert(END,'Items\t\t\t\t'+ 'Cost of Items \n\n')
                       
                        for i in range(8) :
                            try:
                                ep = int(EntryProductList[i].get())
                                eg = int(EntryGoodsList[i].get())
                            except ValueError:
                                messagebox.showwarning(title="Warning", message="Please input the number for the menu field.")
                                ch = 1
                            else:
                                if int(EntryProductList[i].get()) > 0 :
                                    txtReceipt.insert(END, Menu1List[i] +'\t\t\t\t'+ EntryProductList[i].get() + '\n')     
                                if int(EntryGoodsList[i].get()) > 0 :
                                    txtReceipt.insert(END, Menu2List[i] +'\t\t\t\t'+ EntryGoodsList[i].get() + '\n')     
                        if(ch == 0):
                            txtReceipt.insert(END,'\nCost of Drinks : \t\t'+ CostofProduct.get() + '\n')
                            txtReceipt.insert(END,'Cost of Cakes : \t\t'+ CostofGoods.get() + '\n')
                            txtReceipt.insert(END,'Service Charge : \t\t'+ ServiceCharge.get() + '\n')
                            txtReceipt.insert(END,'Paid Tax : \t\t'+ PaidTax.get() + '\n\n')
                            txtReceipt.insert(END,'Total : \t\t'+ TotalCost.get() + "\tbath" + '\n')
                            
                            if(CarRigis.get() == "-"):
                                Check = messagebox.askquestion("Confirm", "Did you confirm that the car was not parked?")
                                if(Check == 'yes'):

                                    try:
                                         out = open("Store.txt", "a" , encoding = "utf-8")
                                    except IOError:
                                        print("Error : can't find file or read data")
                                    else:
                                        print("Written content in the file successfully")
                                        with out as a_file:
                                            a_file.write("\n" + CarRigis.get() + ";" + NameShop + ";" + TotalCost.get() + ";" + str(dateTimeObj))
                                    out.close()
                                    
                                    uploadFile("Store.txt")
                                    
                                else:
                                    CarRigis.set("")
                                     
                            else:
                                have = 0
                                for rigis in li:
                                    if(rigis == CarRigis.get()):

                                        try:
                                            out = open("Store.txt", "a" , encoding = "utf-8")
                                        except IOError:
                                            print("Error : can't find file or read data")
                                        else:
                                            print("Written content in the file successfully")
                                            Checkup = messagebox.askquestion("Confirm", "Confirm information")
                                            if(Checkup == 'yes'):
                                                with out as a_file:
                                                    a_file.write("\n" + CarRigis.get() + ";" + NameShop + ";" + TotalCost.get() + ";" + str(dateTimeObj))
                                                    have = 1
                                                out.close()
                                                uploadFile("Store.txt")
                                                break
                                            else:
                                                have = 2
                                                break
                                                
                                
                                if(have == 1):
                                    messagebox.showwarning(title="Warning", message="Successfully updated information")

                                if(have != 1 and have != 2):
                                    messagebox.showwarning(title="Warning", message="Can not find this car registration")

                            
                #====================== Variable Car registration =====================
                
                CarRigis = StringVar()
                
                #====================== Variable Menu1 ===============================
                    
                ReceiptRef = StringVar()
                DateofOrder = StringVar()
                DateofOrder.set(time.strftime("%d/%m/%Y"))
                
                VarProduct0 = IntVar()
                VarProduct1 = IntVar()
                VarProduct2 = IntVar()
                VarProduct3 = IntVar()
                VarProduct4 = IntVar()
                VarProduct5 = IntVar()
                VarProduct6 = IntVar()
                VarProduct7 = IntVar()
                    
                VarProductList = [VarProduct0, VarProduct1, VarProduct2, VarProduct3, VarProduct4, VarProduct5, VarProduct6, VarProduct7]
                    
                for x in VarProductList:    
                    x.set("0")
                    
                EntryProduct0 = StringVar()
                EntryProduct1 = StringVar()
                EntryProduct2 = StringVar()
                EntryProduct3 = StringVar()
                EntryProduct4 = StringVar()
                EntryProduct5 = StringVar()
                EntryProduct6 = StringVar()
                EntryProduct7 = StringVar()
                    
                EntryProductList = [EntryProduct0, EntryProduct1, EntryProduct2, EntryProduct3, EntryProduct4, EntryProduct5, EntryProduct6, EntryProduct7]
                    
                for x in EntryProductList:    
                    x.set("0")
                
                #====================== Variable Menu2 =================================
                
                VarGoods0 = IntVar()
                VarGoods1 = IntVar()
                VarGoods2 = IntVar()
                VarGoods3 = IntVar()
                VarGoods4 = IntVar()
                VarGoods5 = IntVar()
                VarGoods6 = IntVar()
                VarGoods7 = IntVar()
                
                
                VarGoodsList = [VarGoods0, VarGoods1, VarGoods2, VarGoods3, VarGoods4, VarGoods5, VarGoods6, VarGoods7]
                
                for x in VarGoodsList:    
                    x.set("0")
                
                EntryGoods0 = StringVar()
                EntryGoods1 = StringVar()
                EntryGoods2 = StringVar()
                EntryGoods3 = StringVar()
                EntryGoods4 = StringVar()
                EntryGoods5 = StringVar()
                EntryGoods6 = StringVar()
                EntryGoods7 = StringVar()
                
                
                EntryGoodsList = [EntryGoods0, EntryGoods1, EntryGoods2, EntryGoods3, EntryGoods4, EntryGoods5, EntryGoods6, EntryGoods7]
                
                for x in EntryGoodsList:    
                    x.set("0")
                #===============================Variable Calculation ========================
                
                PaidTax = StringVar()
                SubTotal = StringVar()
                TotalCost = StringVar()
                CostofProduct = StringVar()
                CostofGoods = StringVar()
                ServiceCharge = StringVar()
                
                #============================Car registration================================
                
                lblCarRigis = Label(fCarRigis, font=('times new roman', 16, 'bold'), bg="#392214", text="Car registration",fg="white", bd=16, anchor='w')
                lblCarRigis.grid(row=1, column=0, padx=30)
                textCarRigis = Entry(fCarRigis, font=('times new roman', 16, 'bold'), bd=10, insertwidth=4, textvariable=CarRigis, justify='right').grid(row=1, column=1)
                
                #==================================== Menu1 =================================
                
                Product0 = Checkbutton(fMenu1, padx=15, pady=6, text=Menu1List[0], height=1, bg="#775533", variable = VarProductList[0],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarProductList[0],txtProduct0,EntryProductList[0])).grid(row=1, sticky=W)
                Product1 = Checkbutton(fMenu1, padx=15, pady=6, text=Menu1List[1], height=1, bg="#775533", variable = VarProductList[1],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarProductList[1],txtProduct1,EntryProductList[1])).grid(row=2, sticky=W)
                Product2 = Checkbutton(fMenu1, padx=15, pady=6, text=Menu1List[2], height=1, bg="#775533", variable = VarProductList[2],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarProductList[2],txtProduct2,EntryProductList[2])).grid(row=3, sticky=W)
                Product3 = Checkbutton(fMenu1, padx=15, pady=6, text=Menu1List[3], height=1, bg="#775533", variable = VarProductList[3],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarProductList[3],txtProduct3, EntryProductList[3])).grid(row=4, sticky=W)
                Product4 = Checkbutton(fMenu1, padx=15, pady=6, text=Menu1List[4], height=1, bg="#775533", variable = VarProductList[4],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarProductList[4],txtProduct4, EntryProductList[4])).grid(row=5, sticky=W)
                Product5 = Checkbutton(fMenu1, padx=15, pady=6, text=Menu1List[5], height=1, bg="#775533", variable = VarProductList[5],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarProductList[5],txtProduct5, EntryProductList[5])).grid(row=6, sticky=W)
                Product6 = Checkbutton(fMenu1, padx=15, pady=6, text=Menu1List[6], height=1, bg="#775533", variable = VarProductList[6],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarProductList[6],txtProduct6, EntryProductList[6])).grid(row=7, sticky=W)
                Product7 = Checkbutton(fMenu1, padx=15, pady=6, text=Menu1List[7], height=1, bg="#775533", variable = VarProductList[7],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarProductList[7],txtProduct7, EntryProductList[7])).grid(row=8, sticky=W)
                
                #======================= Enter Widgets for Menu1 =======================

                txtProduct0 = Entry(fMenu1,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryProductList[0], state = DISABLED)
                txtProduct0.grid(row=1, column =1, padx=60)
                txtProduct1 = Entry(fMenu1,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryProductList[1], state = DISABLED)
                txtProduct1.grid(row=2, column =1)
                txtProduct2 = Entry(fMenu1,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryProductList[2], state = DISABLED)
                txtProduct2.grid(row=3, column =1)
                txtProduct3 = Entry(fMenu1,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryProductList[3], state = DISABLED)
                txtProduct3.grid(row=4, column =1)
                txtProduct4 = Entry(fMenu1,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryProductList[4], state = DISABLED)
                txtProduct4.grid(row=5, column =1)
                txtProduct5 = Entry(fMenu1,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryProductList[5], state = DISABLED)
                txtProduct5.grid(row=6, column =1)
                txtProduct6 = Entry(fMenu1,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryProductList[6], state = DISABLED)
                txtProduct6.grid(row=7, column =1)
                txtProduct7 = Entry(fMenu1,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryProductList[7], state = DISABLED)
                txtProduct7.grid(row=8, column =1)
                
                #====================================== Menu2 ====================================
                
                Goods0 = Checkbutton(fMenu2, padx=15, pady=6, text=Menu2List[0], height=1,bg="#775533", variable = VarGoodsList[0] ,onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarGoodsList[0],txtGoods0,EntryGoodsList[0])).grid(row=1, sticky=W)
               
                Goods1 = Checkbutton(fMenu2, padx=15, pady=6, text=Menu2List[1], height=1, bg="#775533", variable = VarGoodsList[1],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarGoodsList[1],txtGoods1,EntryGoodsList[1])).grid(row=2, sticky=W)
                
                Goods2 = Checkbutton(fMenu2, padx=15, pady=6, text=Menu2List[2], height=1, bg="#775533", variable = VarGoodsList[2],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarGoodsList[2],txtGoods2,EntryGoodsList[2])).grid(row=3, sticky=W)
                
                Goods3 = Checkbutton(fMenu2, padx=15, pady=6, text=Menu2List[3], height=1, bg="#775533", variable = VarGoodsList[3],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarGoodsList[3],txtGoods3,EntryGoodsList[3])).grid(row=4, sticky=W)
                
                Goods4 = Checkbutton(fMenu2, padx=15, pady=6, text=Menu2List[4], height=1, bg="#775533", variable = VarGoodsList[4],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarGoodsList[4],txtGoods4,EntryGoodsList[4])).grid(row=5, sticky=W)
                
                Goods5 = Checkbutton(fMenu2, padx=15, pady=6, text=Menu2List[5], height=1, bg="#775533", variable = VarGoodsList[5],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarGoodsList[5],txtGoods5,EntryGoodsList[5])).grid(row=6, sticky=W)
                
                Goods6 = Checkbutton(fMenu2, padx=15, pady=6, text=Menu2List[6], height=1, bg="#775533", variable = VarGoodsList[6],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarGoodsList[6],txtGoods6,EntryGoodsList[6])).grid(row=7, sticky=W)
                
                Goods7 = Checkbutton(fMenu2, padx=15, pady=6, text=Menu2List[7], height=1, bg="#775533", variable = VarGoodsList[7],onvalue = 1, offvalue=0,
                                    font=('times new roman',15,'bold'),command=lambda:chkbutton_value(VarGoodsList[7],txtGoods7,EntryGoodsList[7])).grid(row=8, sticky=W)
                
                #=======================Enter Widgets for Menu2 =======================
                    
                txtGoods0 = Entry(fMenu2, font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryGoodsList[0],state = DISABLED)
                txtGoods0.grid(row=1,column =1, padx=60)
                
                txtGoods1 = Entry(fMenu2,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryGoodsList[1],state = DISABLED)
                txtGoods1.grid(row=2,column =1)
                
                txtGoods2 = Entry(fMenu2,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryGoodsList[2],state = DISABLED)
                txtGoods2.grid(row=3,column =1)
                
                txtGoods3 = Entry(fMenu2,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryGoodsList[3],state = DISABLED)
                txtGoods3.grid(row=4,column =1)
                
                txtGoods4 = Entry(fMenu2,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryGoodsList[4],state = DISABLED)
                txtGoods4.grid(row=5,column =1)
                
                txtGoods5 = Entry(fMenu2,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryGoodsList[5],state = DISABLED)
                txtGoods5.grid(row=6,column =1)
                
                txtGoods6 = Entry(fMenu2,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryGoodsList[6],state = DISABLED)
                txtGoods6.grid(row=7,column =1)
                
                txtGoods7 = Entry(fMenu2,font=('times new roman',15,'bold'),bd=8,width=6,justify='left',textvariable=EntryGoodsList[7],state = DISABLED)
                txtGoods7.grid(row=8,column =1)
                
                #================================== Receipt Information ===================
       
                txtReceipt = Text(fReceipt,font=('times new roman',10,'bold'), bd=8,width=47,height=22, bg="white")
                txtReceipt.grid(row=1,column=0, pady=9)
 
                
                #=================================== Cost Items Information============
                
                lblCostofProduct = Label(fCost1, padx=15, pady=3, font=('times new roman',16,'bold'), text="Cost of " + Type1,bd=8,bg="#392214",fg="white")
                lblCostofProduct.grid(row=0,column=0,sticky=W, padx=25)
                txtCostofProduct=Entry(fCost1,font=('times new roman',16,'bold'),bd=8,justify='left', textvariable=CostofProduct)
                txtCostofProduct.grid(row=0,column=1,sticky=W, padx=10)
                
                lblCostofGoods = Label(fCost1, padx=15, pady=3, font=('times new roman',16,'bold'),text="Cost of " + Type2,bd=8,bg="#392214",fg="white")
                lblCostofGoods.grid(row=1,column=0,sticky=W, padx=25)
                txtCostofGoods=Entry(fCost1,font=('times new roman',16,'bold'),bd=8,justify='left', textvariable=CostofGoods)
                txtCostofGoods.grid(row=1,column=1,sticky=W, padx=10)
                
                lblServiceCharge = Label(fCost1, padx=15, pady=3, font=('times new roman',16,'bold'),text="Service Charge",bd=8,bg="#392214",fg="white")
                lblServiceCharge.grid(row=2,column=0,sticky=W, padx=25)
                txtServiceCharge=Entry(fCost1,font=('times new roman',16,'bold'),bd=8,justify='left', textvariable=ServiceCharge)
                txtServiceCharge.grid(row=2,column=1,sticky=W, padx=10)
                
                #=========================== Payment Information========================
                
                lblPaidTax = Label(fCost1, padx=15, pady=3, font=('times new roman',16,'bold'), text="Paid Tax",bd=8,bg="#392214",fg="white")
                lblPaidTax.grid(row=0,column=2,sticky=W, padx=20)
                txtPaidTax=Entry(fCost1,font=('times new roman',16,'bold'),bd=8,justify='left', textvariable=PaidTax)
                txtPaidTax.grid(row=0,column=3,sticky=W, padx=20)
                
                lblSubTotal = Label(fCost1, padx=15, pady=3, font=('times new roman',16,'bold'),text="Sub Total",bd=8,bg="#392214",fg="white")
                lblSubTotal.grid(row=1,column=2,sticky=W, padx=20)
                txtSubTotal=Entry(fCost1,font=('times new roman',16,'bold'),bd=8,justify='left', textvariable=SubTotal)
                txtSubTotal.grid(row=1,column=3,sticky=W, padx=20)
                
                lblTotalCost = Label(fCost1, padx=15, pady=3, font=('times new roman',16,'bold'),text="Total",bd=8,bg="#392214",fg="white")
                lblTotalCost.grid(row=2,column=2,sticky=W, padx=20)
                txtTotalCost=Entry(fCost1,font=('times new roman',16,'bold'),bd=8,justify='left', textvariable=TotalCost)
                txtTotalCost.grid(row=2,column=3,sticky=W, padx=20)
                
                #================================== Button =========================
                btnTotal=Button(fButton,padx=20, fg="black",bg="#F4A460",font=('times new roman',16,'bold'),width=9, 
                                text="Total",command=CostofItem).grid(row=0, column=0, pady=23, padx=10)
                btnReceipt=Button(fButton,padx=20, fg="black",bg="#F4A460",font=('times new roman',16,'bold'),width=9,
                                text="Receipt",command=Receipt).grid(row=0, column=1, padx=10, pady=10)
                btnReset=Button(fButton,padx=20, fg="black",bg="#F4A460",font=('times new roman',16,'bold'),width=9,
                                text="Reset",command=Reset).grid(row=1, column=0)
                btnExit=Button(fButton,padx=20, fg="black",bg="#F4A460",font=('times new roman',16,'bold'),width=9,
                                text="Exit",command=qExit).grid(row=1, column=1)
                
                
                root.mainloop()
            ipShop.close()
    ftp.close()
    ip.close()
