import lessons.no1 as no1
from rich.prompt import Confirm
from loadInfo import getUserInfo
def start():
    version = '1.1.5'
    print('Starting Python Teacher v'+version)
    # Main Loop
    userInfo = getUserInfo()
    print('Hi')
    print('Users: \n'+str(userInfo.keys()))
    alreadyHere = Confirm.ask('Is your name displayed above?')
    q = Confirm.ask('Are you ready to begin learning '+name+'?')
    if q:
        print('Time to Learn Python!')
        no1.start()
    
    # Closing
    print('Closing Python Teacher')

