# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#create message object instance

msg = MIMEMultipart()

message = 'att Internet Check!'

#configurar os parâmetros da mensagem

password = "987654321SAJ"
msg['From'] = "internetcheck@gmail.com"
msg['To'] = "saviosantossilva19@gmail.com"
msg['Subject'] = "Olá, bom dia!.\n A internet da comunidade de Riachão Malhada BA está muito ruim e com alta instabilidade"

#adicionar no corpo da mensagem

msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP('smatp.gmail.com:587')
server.starttls()

#Credenciais de login para enviar o e-mail
server.login(msg['from', password])

# send the message via the server.
server.sendmail(msg['from'], msg['To'], msg.as_string()) 

server.quit()
print("successfully sent email to %s:" % (msg['To']))