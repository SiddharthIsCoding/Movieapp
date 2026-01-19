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

    global username
    global password

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
            print("\n\n%50s"%"" + Back.RED + Fore.BLACK + " DETAILS MISMATCH , TRY AGAIN ")
            time.sleep(1)
            login()


def logout():
    os.system("cls")
    print("\n\n%50s"%"" + Fore.BLUE + Back.RED + " LOGGING OUT ")
    time.sleep(1)
    login()


seats = [['A1','A2','A3','A4','A5','A6'],
        ['B1','B2','B3','B4','B5','B6','B7','B8'],
        ['C1','C2','C3','C4','C4','C5','C6','C7','C8','C9','C10'],
        ['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12']]


def display():
    
    for i in seats:
        print("\n")
        for m in i: 
            print( Fore.GREEN + "|",m,"|",end="\t")


def booking():
    os.system("cls")
    print("\n")
    print("%50s"%"" + Back.GREEN + Fore.LIGHTGREEN_EX + " BOOK TICKETS ")
    print("\n")
    display()
    print("\n")
    print( "%40s"%"" +  Fore.GREEN + "How many seats do you want ?")
    num= int(input("%40s"%"" + Fore.GREEN + ">>> "))
    print("\n")
    bookings = []
    for i in range(num):
        print("%40s"%"" + Fore.GREEN + "Enter seat number : ")
        s = input("%40s"%"" + Fore.GREEN + ">>> ")
        print("\n")
        bookings.append(s)
    
    mycur.execute("SELECT id FROM users WHERE username = %s AND password = %s ",(username,password))

    id = mycur.fetchone()[0]

    print("id : " , id )

    load_query = "INSERT INTO TABLE orders VALUES(%s,%s,%s)",()
    
    
    
    home()





        



def home():
    os.system("cls")
    print("\n\n%50s"%"" + Fore.GREEN + Back.BLUE + " DASHBOARD ")

    print("\n\n%40s"%"" + Fore.GREEN + "What would you like to do ?")
    print("\n%40s"%"" + Style.DIM + "1> Book Ticket")
    print("\n%40s"%"" + Style.DIM + "2> See Orders")
    print("\n%40s"%"" + Style.DIM + Fore.RED + "3> Log out")

    c = input("\n%40s"%"" + Fore.GREEN + ">>> ")

    if c == "1":
        booking()

    if c == "2":
        pass

    if c == "3":

        logout()
        loggedin = False





while loggedin:
    home()

if not loggedin:
    login()
   







