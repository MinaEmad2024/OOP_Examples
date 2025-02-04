#### a class with just 1 instance

class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception (" the class is Singleton")
        else:
            Singleton._instance = self

s = Singleton.get_instance()
print(s)                
