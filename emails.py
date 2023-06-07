import smtplib
import emails_conf
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Envoyer des emails
# gmail


"""config_email 
config_password
config_serveur
config_serveur_port"""

def envoyer_emails(destinataire, sujet, message):

    multipart_sms = MIMEMultipart()
    multipart_sms["Subject"] = sujet
    multipart_sms["From"] = emails_conf.config_email
    multipart_sms["To"] = destinataire
    multipart_sms.attach(MIMEText(message, "plain"))

    serveur_mail = smtplib.SMTP(emails_conf.config_serveur, emails_conf.config_serveur_port)
    serveur_mail.starttls()
    serveur_mail.login(emails_conf.config_email, emails_conf.config_password)
    serveur_mail.sendmail(emails_conf.config_email, destinataire, multipart_sms.as_string())
    serveur_mail.quit()

message_email = """Bonjour

Comment allez vous ? je serai toujours disponible pour vous.

Merci
"""

envoyer_emails("cletusachot@gmail.com", "Email depuis Python", message_email)

