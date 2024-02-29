"""Create the lesson class.
"""
class part:
    def __init__(self, name="Default", version=str(), projects=[], number=float()):
        self.name = str(name)
        self.version = str(version)
        self.projects = []
        self.number = float(number)
        for project in projects:
            self.addProject(project)
    def addProject(self, project={'start text': 'default', 
                                  'example': 'default',
                                  'you try text': 'default', 
                                  'you try prompt': 'enter default', 
                                  'you try answer': 'default', 
                                  'end text': 'default',}):
        def func():
            print(project['start text'])
            print(project['example'])
            print(project['you try text'])
            answer = input(project['you try prompt']+': ')
            if answer == project['you try answer']:
                print('You got it right!')
                print(project['end text'])
            else:
                while True:
                    print('Try Again.')
                    answer = input(project['you try prompt'])
                    if answer == project['you try answer']:
                        print('You got there.')
                        print(project['end text'])
                        break

            
        self.projects.append(func)
    def run(self):
        print('You got to the next part!')
        print('Time to learn: '+self.name+' '+str(self.number))
        for function in self.projects:
            function()

class lesson:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.parts = []
    def addPart(self, part):
        self.parts.append(part)


if __name__ == '__main__':
    projects = [
        {
            'start text': 'Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}. \n\n An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:\n\n',
            'end text': 'You learnt how to round off floats.',
            'example': '>>>import math\n>>>print(f"The value of pi is approximately {math.pi:.3f}.")\nThe value of pi is approximately 3.142.\n\n',
            'you try text': 'Now try it for yourself',
            'you try prompt': 'Round the integer 4.3252434 to 2 decimal places\nput it in an f-string inside of a print function',
            'you try answer': 'print(f"{4.3252434:.2f}")'
        }
    ]
    test = part('Formatted String Literals', '1', projects, 1)
    test.run()