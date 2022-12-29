# Basic Server Monitor idea

import os
import time
import smtplib
import requests
import paramiko
import smbclient
import ftplib

# List of servers to monitor
servers = ['server1', 'server2', 'server3', 'temp911']

# List of services to monitor
services = ['icmp', 'http', 'smb', 'ftp', 'ssh']

# Email settings
email_username = 'admin@noc.local'
email_password = '********'
email_recipient = 'admin@noc.local'

# Check the status of each server and service
server_status = {}
service_status = {}
for server in servers:
    server_status[server] = 'UP'
    for service in services:
        service_status[server][service] = 'UP'
        
        # Check if the server is responding to ping
        if service == 'icmp':
            response = os.system('ping -c 1 ' + server)
            if response != 0:
                service_status[server][service] = 'DOWN'
                server_status[server] = 'DOWN'
                
        # Check if the server is responding to HTTP requests
        elif service == 'http':
            try:
                response = requests.get('http://' + server)
                if response.status_code != 200:
                    service_status[server][service] = 'DOWN'
                    server_status[server] = 'DOWN'
            except:
                service_status[server][service] = 'DOWN'
                server_status[server] = 'DOWN'
                
        # Check if the server is responding to SMB requests
        elif service == 'smb':
            try:
                with smbclient.Client(server, user='username', password='password') as client:
                    client.list('share')
            except:
                service_status[server][service] = 'DOWN'
                server_status[server] = 'DOWN'
                
        # Check if the server is responding to FTP requests
        elif service == 'ftp':
            try:
                ftp = ftplib.FTP(server)
                ftp.login()
                ftp.quit()
            except:
                service_status[server][service] = 'DOWN'
                server_status[server] = 'DOWN'
