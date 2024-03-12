import pyotp

key = '粘贴 2FA 代码'
totp = pyotp.TOTP(key)
print(totp.now())