import lessons.no1 as no1
def start():
    version = '1.1.2'
    print('Starting Python Teacher v'+version)
    # Main Loop
    name = input('Enter your name: ')
    q = input('Are you ready to begin learning '+name+'? [yes]: ')
    if 'y' in q.lower():
        print('Time to Learn Python!')
        no1.start()
    
    # Closing
    print('Closing Python Teacher')

