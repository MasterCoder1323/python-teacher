"""Create the lesson, and part classes.
"""
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
console = Console()
markdown = Markdown

class Part:
    """Class for creating parts of lessons and displaying them using console and markdown."""

    def __init__(self, name="Default", number=1.1, projects=[]):
        self.name = name
        self.number=number
        self.projects = []
        for project in projects:
            self.add_project(project)

    def add_project(self, project):
        """Adds a project with markdown-formatted content."""

        def run_project():
            # Convert project elements to markdown strings
            start_text = f"\n\n #### {project['start text']}\n"
            example = f"\n{project['example']}\n\n"
            you_try_text = f"{project['you try text']}\n\n"
            prompt = f"{project['you try prompt']}"

            # Combine formatted markdown strings
            content = start_text + example

            # Render the markdown content to console
            console.print('\n\n')
            console.print(markdown(content))
            console.print('\n')
            console.print(markdown(you_try_text))

            # Continue with user interaction as needed
            answer = Prompt.ask(prompt)
            if answer == project["you try answer"]:
                print("[green]You got it right![/green]")
                print(project["end text"])
            else:
                while True:
                    print("[red]Try Again.[/red]")
                    answer = Prompt.ask(prompt)
                    if answer == project["you try answer"]:
                        print("[green]You got there![/green]")
                        print(project["end text"])
                        break

        self.projects.append(run_project)

    def run(self):
        """Prints a heading and runs all projects."""

        heading = f"## {str(self.number)}.  {self.name}\n\n"
        console.print(markdown(heading))

        for project in self.projects:
            project()




class lesson:
    def __init__(self, name='Default', number=1, intro='introduction',parts=[]):
        self.name = name
        self.number = number
        self.parts = parts
        self.intro = intro
    def start(self):
        """Prints the name as a Heading, and then prints the intro as markdown.
        Then runs all parts.
        """
        heading = f"## {str(self.number)}.  {self.name}\n\n"
        console.print(markdown(heading))
        console.print(markdown(self.intro))
        for part in self.parts:
            part.run()


if __name__ == '__main__':
    projects = [
        {
            'start text': 'Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}. \n\n An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:\n\n',
            'end text': 'You learnt how to round off floats.',
            'example': '```python \nimport math\nprint(f"The value of pi is approximately {math.pi:.3f}.")\nThe value of pi is approximately 3.142.',
            'you try text': 'Now try it for yourself',
            'you try prompt': 'Round the integer 4.3252434 to 2 decimal places and put it in an f-string inside of a print function',
            'you try answer': 'print(f"{4.3252434:.2f}")'
        },
        {
            'start text': 'Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}. \n\n An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:\n\n',
            'end text': 'You learnt how to round off floats.',
            'example': '```python \nimport math\nprint(f"The value of pi is approximately {math.pi:.3f}.")\nThe value of pi is approximately 3.142.',
            'you try text': 'Now try it for yourself',
            'you try prompt': 'Round the integer 4.3252434 to 2 decimal places and put it in an f-string inside of a print function',
            'you try answer': 'print(f"{4.3252434:.2f}")'
        }
    ]
    test = Part('Formatted String Literals', '1', projects)
    test.run()