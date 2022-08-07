import sys
from app.requirements import REQ
from os import system


if __name__ == '__main__':
    system('clear')
    try:
        if sys.argv[1] == ('-i' or '-I'):
            REQ().__main__()
        
        
        elif sys.argv[1] == ('runserver' or 'RUNSERVER'):
            system('cd app/API && uvicorn API:C --reload')

        else:
            print("""
        To receive help and informations try something like: python3 main.py [ARGUMENT]

        -i or -I   = Use SUDO to  install packages and dependencias, execute this to the first time or when you forget the private password/key
        
        runserver = To execute the server""")




    except IndexError:
        print("""
        To receive help and informations try something like: python3 main.py [ARGUMENT]

        -i or -I   = Use SUDO to install packages and dependencias, execute this to the first time or when you forget the private password/key
        
        runserver = To execute the server

        """)
   


