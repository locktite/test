# create pkcs with python and store files in /home/user1/cert
#

# Import required libraries
import OpenSSL

# Generate private key
key = OpenSSL.crypto.PKey()
key.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)

# Generate certificate
cert = OpenSSL.crypto.X509()
cert.get_subject().CN = "Your Name"
cert.set_serial_number(1000)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(10*365*24*60*60)
cert.set_issuer(cert.get_subject())
cert.set_pubkey(key)
cert.sign(key, "sha256")

# Save private key and certificate to PKCS12 file
pkcs = OpenSSL.crypto.PKCS12()
pkcs.set_privatekey(key)
pkcs.set_certificate(cert)
pkcs_file = open("/home/user1/cert/pkcs.p12", "wb")
pkcs.write_pem(pkcs_file)
pkcs_file.close()

