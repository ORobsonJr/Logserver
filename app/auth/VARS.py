from os import system, getcwd


class Parameters():
    def __init__(self):
        pass
   
    def values(self, key: str, file_location: str = ''):
        print(file_location)
        if file_location:
            fl_ = file_location.replace('/auth/data.config.aes', 'app/auth/data.config')
            


        else: 
            fl_ = str(getcwd()).replace('/API', 'app/auth/data.config')
            system(f"aescrypt -d -p {key} {fl_}.aes") #Decrypt the crypted file



        with open(fl_, 'r') as f:
            READ = f.readlines()
            HOST = READ[0].replace('\n', '').replace(' ', '').split(':')
            USER = READ[1].replace('\n', '').replace(' ', '').split(':')
            PASSWORD = READ[2].replace('\n', '').replace(' ', '').split(':')
            DATABASE = READ[3].replace('\n', '').replace(' ', '').split(':')
            f.close()
        
        system(f"rm {fl_}")
        return [HOST[1], USER[1], PASSWORD[1], DATABASE[1]]





        

