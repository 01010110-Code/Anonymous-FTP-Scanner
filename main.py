import ftplib

def scan_ftp(host):
  try:
    ftp = ftplib.FTP(host)
    ftp.login()
    print(f'Found anonymous FTP server at {host}')
  except Exception as e:
    print(f'Anonymous FTP not found at {host}')

# Scan localhost
scan_ftp('127.0.0.1')

# Scan a range of IP addresses
for i in range(1, 255):
  scan_ftp(f'192.168.0.{i}')
