from ftplib import FTP
import time,threading

class Pop(threading.Thread):
    def __init__(self,status,uploading,uploaded):
        threading.Thread.__init__(self)
        self._status = status
        self._uploading = uploading
        self._uploaded = uploaded

    def loginServer (self) :
        # *************************************** FOR LOGIN ***************************************
        FTPServer = '158.108.97.18'
        Username  = 'ST03603423' 
        Password = '03603423'
        try:
            ftp = FTP(FTPServer)
            ftp.login(user = Username, passwd = Password)
            ftp.cwd('Assigngroup1')
            self._ftp = ftp
            # print('login success')
        except:
            print("Can not Login!!!\n")
        
    def clearReceipt(self):
        try:
            os.remove('Receipt.txt')
            name = open('Receipt.txt','w',encoding="utf-8")
            name.close()
            self.uploadFile('Receipt.txt')
        except:
            print("Clear Receipt error")
                
    def downloadFile(self,filename):
        # *************************************** FOR DOWNLOAD FILE ***************************************
        try:
            localfile = open(filename, 'wb')
            self._ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
            self._uploaded.value = 1
        except:
            print("Can not download file! : ",filename)
            localfile.close()
                
    def uploadFile(self,filename):
        # *************************************** FOR UPLOAD FILE ***************************************
        try:
            self._ftp.storbinary('STOR ' + str(filename), open("Output.txt", 'rb'))
            self._uploading.value = 0
        except:
            print("Can not upload file!")  

    def run (self):
        # *************************************** RUN ***************************************
        print('start run')
        while(True):
            try :
                print('status start = ',self._status.value)
                self._ftp.voidcmd("NOOP")
                if self._uploading.value ==0:
                    self.downloadFile('Store.txt')
                    self.downloadFile('Park.txt')
                self._status.value = 1
            except :
                print('Disconnected Reconnecting . . . \n')
                self._status.value = 0
                self.loginServer()
            time.sleep(10)

