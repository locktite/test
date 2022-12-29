# Import the necessary modules
import pyotp
import smtplib

# Generate a random secret key
secret_key = pyotp.random_base32()

# Save the secret key to a file
with open('secret.txt', 'w') as f:
    f.write(secret_key)

# Create a TOTP object using the secret key
totp = pyotp.TOTP(secret_key)

# Generate the current OTP
otp = totp.now()

# Print the OTP
print(otp)

# Email settings
email_username = '2fa@server.local'
email_password = '********'
email_recipient = 'user@client.local'

# Send the OTP via email
server = smtplib.SMTP('smtp.server.local')
server.starttls()
server.login(email_username, email_password)
server.sendmail(
    email_username,
    email_recipient,
    'Subject: 2FA OTP\n\nYour OTP is ' + otp
)
server.quit()

