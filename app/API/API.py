from fastapi import FastAPI
from pydantic import BaseModel
import sys
sys.path.insert(0, '../')
from database.actions import DB
from auth.VARS import Parameters
from typing import Optional


C = FastAPI()
data = Parameters().values(input('Type your secret password: '))
database_connection = DB(database_name=data[3], user=data[1], password=data[2], host=data[0])



class var(BaseModel):
    email: str
    password: str
    name: str
    telephone: Optional[int] = 0 




class API(BaseModel): 
    @C.get('/checkUser/')
    async def check_user(email: str = '', telephone: str = ''):
        if email:
            value = database_connection.check_user_existence(email=email)
            return {'Status_User': value}
    
        value = database_connection.check_user_existence(telephone=telephone)
        return {'Status_User': value}

    @C.get('/loginUser/')
    async def login(email: str, password: str):
        value = database_connection.login_user(email=email, password=password)
        return {'Status_login': value}

    @C.post('/signUp/')
    async def create_account(data: var):
        value = database_connection.register(
            email=data.email, 
            password=data.password,
            name=data.name,
            telephone=data.telephone
        )
        
        return {'STATUS_SIGN_UP':value}


        
        


