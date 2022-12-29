# create python file that compress and backup logs folder to zip file add to zip file date and time as file name, transfer via ftp ,
# delete local uploaded zip and old logs after upload success
#
# Import required libraries
import os
import time
import zipfile
import ftplib
import shutil

# Set input and output directories
input_dir = "./logs"
output_dir = "./backup"

# Create output directory
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set current date and time
date_time = time.strftime("%Y-%m-%d_%H-%M-%S")

# Set output file name
output_file = os.path.join(output_dir, "logs_%s.zip" % date_time)

# Create ZIP file
with zipfile.ZipFile(output_file, "w") as zip_file:
    # Loop through files in input directory
    for root, dirs, files in os.walk(input_dir):
        # Loop through files
        for file in files:
            # Set input and output paths
            input_path = os.path.join(root, file)
            output_path = os.path.relpath(input_path, input_dir)

            # Add file to ZIP file
            zip_file.write(input_path, output_path)

# Set FTP server information
ftp_server = "ftp.yourserver.com"
ftp_username = "your_username"
ftp_password = "your_password"

# Connect to FTP server
ftp = ftplib.FTP(ftp_server)
ftp.login(ftp_username, ftp_password)

# Set FTP directory
ftp_dir = "/logs/"

# Change to FTP directory
ftp.cwd(ftp_dir)

# Open ZIP file
with open(output_file, "rb") as zip_file:
    # Upload ZIP file
    ftp.storbinary("STOR logs.zip", zip_file)

# Close FTP connection
ftp.quit()

# Delete local uploaded ZIP file
os.remove(output_file)

# Delete old logs
shutil.rmtree(input_dir)
