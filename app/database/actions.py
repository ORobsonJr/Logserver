import mysql.connector, sys


"""
Handle some commands like check the existence of user, sign in and create account
"""

class DB():
    def __init__(self, host, database_name, user, password):
        self.host = host
        self.database_name = database_name
        self.user = user
        self.password = password

        self.connection = mysql.connector.connect(
        host = self.host,
        user = self.user,
        password = self.password,
        database = self.database_name,
        use_pure = True
        )
        self.cursor = self.connection.cursor()

    def check_user_existence(self, email: str = '', telephone: int = 0):
        if email:
            self.cursor.execute("SELECT EMAIL FROM USERS WHERE EMAIL='{}'".format(email))
            if len(self.cursor.fetchall()) >=1:
                return True

        elif telephone:
            telephone: str

            self.cursor.execute("SELECT TELEPHONE FROM USERS WHERE TELEPHONE='{}'".format(telephone))
            if len(self.cursor.fetchall()) >=1:
                return True
        else:
            return 'NoData'

        
        return False

    def login_user(self, email: str, password: str):
        if email and password:
            if DB().check_user_existence(email=email) ==True:
                self.cursor.execute("SELECT EMAIL AND PASSWORD FROM USERS WHERE EMAIL='{EMAIL}' AND PASSWORD='{PASSWORD}';".format(EMAIL=email, PASSWORD=password))
                if len(self.cursor.fetchall()) >=1:
                    return True
                return False
            else:
                return 'UserNotFound'
        return 'NoParameters'

    def register(self, email: str, password: str,name: str, telephone:str = ''):
        if DB.check_user_existence(self, email=email) ==True: #Check if user already exist
            return "ThisAccountAlreadyExists"

        #Filter data to avoid bad information
        if email.find('@') ==-1: return 'TypeValidEmail'
        if len(name) <3: return 'TypeNameError'
        if any(map(str.isdigit, name)) == True: return "NumbersInNameError"


        #Create register without telephone
        if email and password and name:
            self.cursor.execute(f"INSERT INTO USERS (NAME, PASSWORD, EMAIL) VALUES ('{name}', '{password}', '{email}');")
            self.connection.commit()

            return 'AccountCreated'

        elif telephone:#Create register with telephone
            if len(str(telephone)) <=5: return 'Inserta valid phone number' 
            self.cursor.execute(f"INSERT INTO USERS (NAME, PASSWORD, EMAIL, TELEPHONE) VALUES ('{name}', '{password}', '{email}', '{telephone}');")
            self.connection.commit()

            return 'AccountCreatedWithNumber'


        else:
            return 'NoDataWasSend'
    




    
