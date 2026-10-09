import smtplib
from email.message import EmailMessage


def send_email(to_email, subject, body):
    my_email = "bogdanmyrka186@gmail.com"
    my_password = "dyam mzwu mwgw ohcu" 
    
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = my_email
    msg["To"] = to_email
    
    
    
    try:
        with open("qr.png", "rb") as f:
            file_data = f.read()
            file_name = "qr.png"
            
        msg.add_attachment(
            file_data, 
            maintype="image", 
            subtype="png", 
            filename=file_name
        )
    except FileNotFoundError:
        print("Предупреждение: Файл qr.png не найден, отправка без вложения.")
    
    try:
        print("Send message")
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(my_email, my_password)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send the message {e}")
        
send_email(
    "patdesathonor6@gmail.com",
    "Bogdan sends you the message",
    f"ваш код авторизации RUVQFDSGEEOGRUTXGBXE6VJMV4QTENZH"
)