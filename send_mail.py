import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
sender = "songsongbearbear04@gmail.com"        #把寄件者設立代號
receiver = ["nishiontsukasajp@gmail.com","songsongbearbear04@gmail.com"]

for ctt in receiver:        #後面帶入要重複作業地方
    msg = MIMEMultipart()
    msg["From"] = sender   #寄件人
    msg["To"] = ctt      #收件人
    header = Header("Test send Email","utf-8")     #主旨跟使用UTF-8編碼
    msg["Subject"] = header.encode()

    body = "This is email send from python"        #內文
    msg.attach(MIMEText(body))                     #此行等於下列兩行
#mbody = MIMEText(body)
#msg.attach(mbody)
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:    #465 為goole用編號
        server.login(sender,"vnyd ydzg pqap ktne")        #登入該帳號及應用程式密碼
        server.sendmail(sender,ctt,msg.as_string())     #寄件人與收件人和執行格式
    print("success send email")