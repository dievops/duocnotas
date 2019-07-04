from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

usuario = "nombredeusuario"
contrasena = "contraseña"

driver = webdriver.Chrome()
driver.get("http://cuentas.duoc.cl/misnotas/")
username = driver.find_element_by_name("user")
password = driver.find_element_by_name("pass")

username.send_keys(usuario)
password.send_keys(contrasena)

driver.find_element_by_name("Aceptar").click()

#enviar correo
host = "smtp.gmail.com"
port = 465
smtp_user = "nombre@gmail.com"
smtp_password = "password-correo"
server = smtplib.SMTP()
server.connect(host,port)
server.login(smtp_user,smtp_password)

msg = MIMEMultipart('alternative')
text = "Subject=Notas Duoc\nHola.\nEspero te encuentres muy bien!\nAquí están tus notas de Duoc al Día de hoy"
html = driver.page_source
# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

server.sendmail("de", "para", msg.as_string())
driver.close()
