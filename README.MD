<img src="https://github.com/darkseid-security/DarkVoid/blob/main/IMG/Screenshot%20at%202022-12-04%2005-17-11.png">
[DarkVoid]

Mass FTP exploitation tool, automates exploiting FTP servers.

Features:
- Detects FTP service version and alerts you if server is vulnerable to RCE(Remote Code Execution)
- Automatic exploitation
- Built in exploits
- Tries anonymous login
- Tries to upload a shell if anonymous login is successful
- Bruteforce default creds
- If bruteforce is successful program will try and upload a reverse shell through FTP for every cracked account
- Logs cracked user accounts and compromise FTP server via backdoor shell

Supports:
- All operating systems running python enviroment
- Exploit support for Pureftp,Proftp,filezilla,titan and cerberus FTP
- Exploits for Windows and Linux

TODO:
- Add more exploits
- Import Windows exploits(currently not usable)
- Test proFTPD 1.3.2rc3 exploit 

*Change msfvenom_host and msfvenom_port variable in exploit.py to callback to server and port for the php meterpreter reverse shell
