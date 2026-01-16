import mysql.connector , random , os , time
from colorama import *

init(autoreset=True)

os.system("cls")

loggedin = False






try: 

    myconn = mysql.connector.connect(host="localhost",
                                     username="root",
                                     passwd="root",
                                     db="project0")
    
    if myconn:
        print('\n'+Fore.GREEN+Back.BLUE+'\tCONNECTED')
    
    mycur = myconn.cursor()


    def login():
       os.system('cls')
       print( "\n\n%50s"%""+ Back.GREEN + Fore.LIGHTGREEN_EX + " LOGIN ")

       print( "\n%45s"%""+ Fore.GREEN + "Enter username ")
       username = input("%40s"%""+ Fore.GREEN+ ">>> ")
    
       print( "\n%45s"%""+ Fore.GREEN + "Enter password")
       password = input( "%40s"%""+Fore.GREEN+">>> ")

       mycur.execute("INSERT INTO users VALUES(%d,%s,%d)"%(random.randrange(99,1000),username,password))
       print("Loaded")


    login()


   


except:

    print("\n\n\n" + Fore.RED + Back.GREEN + "CONNECTION FAILED")






