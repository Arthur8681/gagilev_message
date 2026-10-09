import pyotp 

def verify(secret, user_code):
    totp = pyotp.TOTP(secret)
    return totp.verify(user_code)


secret ="RUVQFDSGEEOGRUTXGBXE6VJMV4QTENZH"

user_code = input()

if verify(secret, user_code):
    print("Вход")
else:
    print("error")
    
