import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# this is why i get banned from people inboxes.

sender_email = "...@gmail.com" # your gmail here
sender_password = "kjuiwhxnoqjdklad" # app password here (16 characters + 2FA)
receiver_email = "...@gmail.com" # your target gmail >:D
subject = "Good day, Fuhrer."
message = "Testing Testing nein nein mein kampf 卐"

msg = MIMEMultipart()
msg['From'] = "N.Petrov [☭]"
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

try:
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(sender_email, sender_password)
   server.sendmail(sender_email, receiver_email, msg.as_string())
   print("SUCCESS M8")
except Exception as e:
   print("FAILED M8:", e)
finally:
   server.quit()


# for multi dudes, im tired...

"""
RECEIVERS = ["retard1@example.com", "retard2@example.com"] # replace with real addresses
TEMPLATE = "Hello {name}, this is an automated test message."
DELAY_BETWEEN_SENDS = 1.0 # seconds

def is_valid_email(addr: str) -> bool:
    return bool(re.fullmatch(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", addr))

password = os.environ.get("EMAIL_PASSWORD") or getpass("Enter app password (hidden): ")

for rcpt in RECEIVERS:
    if not is_valid_email(rcpt):
        print("Skipping invalid address:", rcpt)
        continue
"""
