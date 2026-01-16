import mysql.connector , random , os , time
from colorama import *

init(autoreset=True)

os.system("cls")

loggedin = False






try: 

    myconn = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="root",
                                     db="project0")
    
    if myconn:
        print('\n'+Fore.GREEN+Back.BLUE+'\tCONNECTED')
except:

    print("\n\n\n" + Fore.RED + Back.GREEN + "CONNECTION FAILED")


    
mycur = myconn.cursor()



def login():
    os.system('cls')
    print( "\n\n%50s"%""+ Back.GREEN + Fore.LIGHTGREEN_EX + " LOGIN ")

    print( "\n%45s"%""+ Fore.GREEN + "Enter username ")
    username = input("%40s"%""+ Fore.GREEN+ ">>> ")
    
    print( "\n%45s"%""+ Fore.GREEN + "Enter password")
    password = input( "%40s"%""+Fore.GREEN+">>> ")

    mycur.execute("SELECT username,password FROM users;")

    data = mycur.fetchall()


    for i in data:
        if username and password in i:
            os.system("cls")
            print("\n%50s"%"" + Back.GREEN + Fore.BLUE + " LOG IN SUCCESFUL ")
            time.sleep(1)
            loggedin = True
            home()
            break

        else:
            os.system("cls")
            print("\n\n%50s"%"" + Back.RED + Fore.BLUE + " DETAILS MISMATCH , TRY AGAIN ")
            time.sleep(1)
            login()


def logout():
    os.system("cls")
    print("\n\n%50s"%"" + Fore.BLUE + Back.RED + " LOGGING OUT ")
    time.sleep(1)
    loggedin = False


def display():
    pass



def home():
    os.system("cls")
    print("\n\n%50s"%"" + Fore.GREEN + Back.BLUE + " DASHBOARD ")

    print("\n\n%40s"%"" + Fore.GREEN + "What would you like to do ?")
    print("\n%40s"%"" + Style.DIM + "1> Book Ticket")
    print("\n%40s"%"" + Style.DIM + "2> See Orders")
    print("\n%40s"%"" + Style.DIM + Fore.RED + "3> Log out")

    c = input("\n%40s"%"" + Fore.GREEN + ">>> ")

    if c == "1":
        pass

    if c == "2":
        pass

    if c == "3":

        logout()






while True:

    if loggedin:
        home()
    else:
        login()
   







