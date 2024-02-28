from setuptools import setup, find_packages

setup(
    name="python-teacher",  # Replace with your package name
    version="1.1.0",  # Replace with your initial version
    description="A command line program to teach you python.",  # Replace with your description
    author="Master Coder 1323",  # Replace with your name
    author_email="sparlevi18@gmail.com",  # Replace with your email
    packages=find_packages(),  # Automatically finds packages in your project structure
    install_requires=['sys'],  # List any external libraries required (empty for now)
    # scripts=['main.py'],
    entry_points={
        'console_scripts': [
            'python-teacher = ',
        ],
    },
)
