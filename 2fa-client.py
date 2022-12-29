# Import the necessary modules
import pyotp

# Read the secret key from the file
with open('secret.txt', 'r') as f:
    secret_key = f.read()

# Create a TOTP object using the secret key
totp = pyotp.TOTP(secret_key)

# Prompt the user for the OTP
otp = input('Enter the OTP: ')

# Verify the OTP
if totp.verify(otp):
    print('OTP verified')
else:
    print('Invalid OTP')

