from lessons.lesson import Part, lesson

invokingProjects = [
    {
        'start text': 'The Python interpreter is usually installed as /usr/local/bin/python3.12 on those machines where it is available; putting /usr/local/bin in your Unix shell’s search path makes it possible to start it by typing the command: `python3` on unix systems, and `python` or `py` on windows.',
        'end text': 'Since the choice of the directory where the interpreter lives is an installation option, other places are possible; check with your local Python guru or system administrator. (E.g., /usr/local/python is a popular alternative location.) \
\
On Windows machines where you have installed Python from the Microsoft Store, the python3.12 command will be available. If you have the py.exe launcher installed, you can use the py command. See Excursus: Setting environment variables for other ways to launch Python. \
\
Typing an end-of-file character (Control-D on Unix, Control-Z on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn’t work, you can exit the interpreter by typing the following command: quit().\
\
The interpreter’s line-editing features include interactive editing, history substitution and code completion on systems that support the GNU Readline library. Perhaps the quickest check to see whether command line editing is supported is typing Control-P to the first Python prompt you get. If it beeps, you have command line editing; see Appendix Interactive Input Editing and History Substitution for an introduction to the keys. If nothing appears to happen, or if ^P is echoed, command line editing isn’t available; you’ll only be able to use backspace to remove characters from the current line. \
\
The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a script from that file.\
\
A second way of starting the interpreter is python -c command [arg] ..., which executes the statement(s) in command, analogous to the shell’s -c option. Since Python statements often contain spaces or other characters that are special to the shell, it is usually advised to quote command in its entirety. \
\
Some Python modules are also useful as scripts. These can be invoked using python -m module [arg] ..., which executes the source file for module as if you had spelled out its full name on the command line.\
\
When a script file is used, it is sometimes useful to be able to run the script and enter interactive mode afterwards. This can be done by passing -i before the script.\
\
All command line options are described in Command line and environment.',
        'example': '```bash \npython3\npython\npy',
        'you try text': 'Now try it for yourself',
        'you try prompt': 'Invoke the interpreter on a unix like system',
        'you try answer': 'python3'
    }
]
invoking = Part('Invoking the Interpreter',2.1,invokingProjects)