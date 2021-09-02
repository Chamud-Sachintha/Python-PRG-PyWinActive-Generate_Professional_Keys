import subprocess,socket,sys
import requests

def CheckInternetConenctionForHost():
    URL = "https://getcid.info"
    timeout = 5

    try:
        MakeRequest = requests.get(URL, timeout=timeout)
        return True
    except(requests.ConnectionError, requests.Timeout):
        return False

def ReturnURLForInstallationID(InstallationID,AuthenticationCode):
    DefaultUrl = "https://getcid.info/api/" + InstallationID + "/" + AuthenticationCode

    return DefaultUrl

def MakeGETRequestForTheURL(url):
    WebRequest = requests.get(url)

    return WebRequest

def main():
    subprocess.run(['color', 'a'], shell=True)

    while True:
        banner = (r'''

=========================================================================================================

            GitHub :- https://github.com/Chamud-Sachintha/Python-PRG-PyWinActive WinKeyGenerator
            
    
  /$$$$$$$           /$$       /$$/$$            /$$$$$$              /$$     /$$                    
| $$__  $$          | $$  /$ | $$|__/           /$$__  $$            | $$    |__/                    
| $$  \ $$ /$$   /$$| $$ /$$$| $$ /$$ /$$$$$$$ | $$  \ $$  /$$$$$$$ /$$$$$$   /$$ /$$    /$$ /$$$$$$ 
| $$$$$$$/| $$  | $$| $$/$$ $$ $$| $$| $$__  $$| $$$$$$$$ /$$_____/|_  $$_/  | $$|  $$  /$$//$$__  $$
| $$____/ | $$  | $$| $$$$_  $$$$| $$| $$  \ $$| $$__  $$| $$        | $$    | $$ \  $$/$$/| $$$$$$$$
| $$      | $$  | $$| $$$/ \  $$$| $$| $$  | $$| $$  | $$| $$        | $$ /$$| $$  \  $$$/ | $$_____/
| $$      |  $$$$$$$| $$/   \  $$| $$| $$  | $$| $$  | $$|  $$$$$$$  |  $$$$/| $$   \  $/  |  $$$$$$$
|__/       \____  $$|__/     \__/|__/|__/  |__/|__/  |__/ \_______/   \___/  |__/    \_/    \_______/
        /$$     | $$                                                                                 
            |$$$$$$/                                                                                 
           \______/      

                                        Develop By :- Sh3rl0k
                                        Version :- 1.0 v

=========================================================================================================== 

        ''')

        print(banner)
        sys_inp = input("Press 'y' to continue or 'n' to cancle :- ")

        if(sys_inp == 'y'):
            print('')
            print("Checking Internet Connection...")
            print('')
            if(CheckInternetConenctionForHost() == True):
                IPAddress = socket.gethostbyname(socket.gethostname())
                print("Connection Successfully...")
                print("Host IP Address :- ", IPAddress)
                print("")

                set_AuthCode = "testAuth123"
                InstallationID = input("Enter Installation ID Number (Without '-' and Spaces) :- ")

                if(InstallationID != ""):
                    GetActualURL = ReturnURLForInstallationID(InstallationID,set_AuthCode)
                    ConfirmationNumber = MakeGETRequestForTheURL(GetActualURL)

                    print("")
                    print("Your Confirmation Number Is :- ", ConfirmationNumber.text)
                    print("")
                else:
                    print("")
                    print("Please Enter Installation ID Before Continue...")
            else:
                print("")
                print("This PC Is Not Connected To The Internet.")
        else:
            sys.exit()

if __name__ == '__main__':
    main()