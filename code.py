import random 
import pyotp, qrcode

def generate_totp():
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    uri = totp.provisioning_uri(
    name="MyApp",
    issuer_name="gagileveu@mail.ru"
    )
    
    img = qrcode.make(uri)
    img.save("qr.png")
    print(secret)



generate_totp()