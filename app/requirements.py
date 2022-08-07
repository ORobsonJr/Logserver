from os import system, getcwd
import sys
sys.path.insert(0, '../')
from app.auth.VARS import Parameters
import pkg_resources
from app.dir.directorys import directorys


#colors
gr = '\033[1m'+'\033[32m' #green
re = '\033[1m'+'\033[31m' #red
wh = '\033[1m'+'\033[37m' #white
yl = '\033[1m'+'\033[33m' #Yelllow


class REQ():
    def __init__(self):
        self.user = ''
        self.password = ''
        self.host = ''
        self.private_password = ''
         
        call = directorys()
        self.encrypted_file = call.auth()['encrypted_file']
        self.decrypted_file = call.auth()['decrypted_file']

    

    def uvicorn(self):
        c = str(system('which uvicorn'))
        if len(c)<1:
            print(re+'[!]Uvicorn not found')
            print(wh+str(system('sudo pip3 install uvicorn')))
            print(gr+'Uvicorn installed sucessfully')
            return None
        print(gr+'Uvicorn already installed')

    def mysql_server(self):
        c = str(system('which mysql'))
        
        if len(c) >=1:
            print(gr+'MySql server already installed. passing...')
            return None
        print(wh+str(system('sudo apt update && sudo apt install mysql-server')))
        print(wh+str(system('sudo mysql_secure_installation')))
        print(re+"We don't privilegies enough to install this completely, then check the documentation <https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-pt> and try after.")
        

    def python_libraries(self):
        required = {'pydantic', 'fastapi', 'mysql-connector'}
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = required - installed
        print(wh+'Checking installed python libraries...')
        print(wh+'[{}] Dependencies founded'.format(len(missing)))
        
        if len(missing) >=1:
            for package in missing:
                print(wh+str(system(f'sudo pip3 install {package}')))
        print(gr+'All python libraries installed')

    def aescrypt(self):
        c = str(system('which aescrypt'))
        if len(c) >=1:
            print(gr+'Aescrypt already installed founded in ', c)
            return None
        print(wh+'Installing aescrypt...')
        print(wh+str(system('mkdir download_file')))
        print(wh+str(system('cd download_file && wget https://www.aescrypt.com/download/v3/linux/AESCrypt-GUI-3.11-Linux-x86_64-Install.gz')))
        print(wh+str(system('gunzip AESCrypt-GUI-3.11-Linux-x86_64-Install.gz')))
        print(wh+str(system('chmod +x AESCrypt-GUI-3.11-Linux-x86_64-Install')))
        print(wh+str(system('./AESCrypt-GUI-3.11-Linux-x86_64-Install')))
        print(wh+'Aescrypt installed sucessfully')
        print(wh+str(system('rm -r download_file')))



        if len(system('which aescrypt')) >=1:
            print(gr+'Aescrypt installed succesfully!!')
        else:
            print(re+"[!]Unfortunately don't was possible install this program :(, please check the documentation here <https://www.aescrypt.com/documentation/AES%20Crypt%20User%20Guide.pdf> ou try manually")


    def config_data(self):
        print(yl+"""
                Here i'm considering the fact that you already had a database created and configured with the privilligies below:

                * User with sufficient privilegies to manipulate the database
                * A database created
                * MySQl setuped

                If you don't create it, please visit: 
                https://netbeans.apache.org/kb/docs/ide/install-and-configure-mysql-server.html
        """)

        def data_file():
            print(yl+"Now you need type the data of your MySQL database!")
            self.user = input(wh+'\nNow type the username of authentication(ex.: root):  ')
            self.password = input(wh+'\nEnter your database password if you have it, if not press <ENTER> :')
            self.host = input(wh+'\nSelect the name of your host(ex.: localhost or 127.0.0.1):  ')
            self.private_password = input(wh+'\nCreate a secret key to use your API, this password will required when you try start the server:  ')

        mode = input('Do you already install and setup MYSQL with the requisites above?:(Y/N): ')

        if mode.find('Y')!=-1 or mode.find('y') !=-1:
            data_file()
        else:
            print(re+'Configure your MYSQL requisites and run main.py -i again')
            sys.exit()

        print(wh+'\n\nScrapping parameters...')
        print(wh+'Creating data.config....')
        print(wh+str(system('cd app/auth && touch data.config')))
        print(gr+'Data.config create sucessfully')

        dir = str(getcwd())
       

        def create_file(self):
            with open(dir+f'/{self.decrypted_file}', 'w') as f:
                f.write(f'HOST: {self.host}\n')
                f.write(f'USER: {self.user}\n')
                f.write(f'PASSWORD: {self.password}\n')
                f.write(f'DATABASE: USER_DATA')

        create_file(self)

        print(wh+str(open(dir+f'/{self.decrypted_file}', 'r').read()))
        print(wh+"SECRET_PASSWORD: ",self.private_password)

        edit = input(gr+"\nThe DATABASE 'USER_DATA' are the default database, then don't change it \nAre the data above correct?(y/n): ")

        if edit == ('n' or 'no' or 'NO' or 'N'):
            data_file(self)
            create_file(self)
        
        print("Let's encrypt the data with sensitive informations")
        print(re+"[!]WARNING THE DATA.CONFIG WILL BE ENCRYPTED AND ALL SOFTWARE WILL BE AFFECTED IF YOU DON'T REMEMBER THE RIGHT PASSWORD")
        mode = input('Skip instead redefine your private password?(y/n): ')
        if mode !=('y' or 'Y' or'yes' or 'YES'):
            self.private_password = input('Type your new private password: ')

        system(f'cd auth && aescrypt -e -p {self.private_password}  {self.encrypted_file}')
        print(gr+'Data.config was encrypt')
        system(f'rm {dir}/{self.decrypted_file}')
        print(gr+'Insecure data.config was permatently deleted')
        print("All done, closing...")

    def create_database(self):
        def separe_data():
            v = Parameters().values(key=input(str('Type your secret key: ')), file_location=(self.decrypted_file))
            self.host = v[0]
            self.user = v[1]
            self.password = v[2]

        separe_data()


        import mysql.connector

        DB = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            use_pure = True
        )

        cursor = DB.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS USER_DATA;')
        DB.commit()
        print(wh+'Database USERS create sucessfully')


        cursor.execute('CREATE TABLE IF NOT EXISTS USER_DATA.USERS (ID int NOT NULL, NAME varchar(255) NOT NULL, EMAIL varchar(255) NOT NULL,TELEPHONE int, PASSWORD varchar(255) NOT NULL, PRIMARY KEY (ID));')
        DB.commit()
        print(wh+'Table and columns created')

        print(gr+'Database done!')



            
    def __main__(self):
        system('clear')
        try:
            obj = REQ()
            """ obj.python_libraries()
            obj.aescrypt()
            obj.uvicorn()
            obj.mysql_server() """
            #obj.config_data() 
            obj.create_database()

        except KeyboardInterrupt:
            sys.exit


        