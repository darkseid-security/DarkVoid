
import requests
from colorama import Fore

def web_request(host):
    try:
        r = requests.get("http://" + (host))
        header = r.headers['Server']
        if 'Apache' in header:
            print(Fore.YELLOW + "[!] " + Fore.RESET + "Webserver: " + Fore.YELLOW + header + Fore.RESET)
            print(Fore.YELLOW + "[!] " + Fore.RESET + "Exploit Method:" + Fore.YELLOW + " Upload PHP Backdoor" + Fore.RESET)
        elif 'nginx' in header:
            print(Fore.YELLOW + "[!] " + Fore.RESET + "Webserver: " + header + " Upload PHP Shell to Compromise Server")
            print(Fore.YELLOW + "[!] " + Fore.RESET + "Exploit Method:" + Fore.YELLOW + " Upload PHP Backdoor" + Fore.RESET)
    except:
        print(Fore.YELLOW + "[!] " + Fore.RESET + "HTTP Server Unreachable")
