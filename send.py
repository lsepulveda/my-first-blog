import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from email.Encoders import encode_base64
from email.mime.application import MIMEApplication

msg = MIMEMultipart()
msg['From']="sepulveda.carlos.larenas@gmail.com"
msg['To']="sepulveda.carlos.larenas@gmail.com"
msg['Subject']="asuntos"

#msg.attach(MIMEText(file("/home/csepulveda/project/test.pdf").read()))
part = MIMEApplication(open("test.pdf","rb").read())
part.add_header('Content-Disposition', 'attachment', filename="test.pdf")
msg.attach(part)
mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login("sepulveda.carlos.larenas@gmail.com","Lin@res.1995")

mailServer.sendmail("sepulveda.carlos.larenas@gmail.com", "sepulveda.carlos.larenas@gmail.com", msg.as_string())

mailServer.close()

