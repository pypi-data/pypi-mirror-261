import binascii
from backports.pbkdf2 import pbkdf2_hmac

# Passcode
def authenticate(pw):

    expected_key = ""

    salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
    passwd = pw.encode("utf8")
    key = pbkdf2_hmac("sha256", passwd, salt, 50000, 32)

    if key == expected_key:
        return True
    else:
        return False