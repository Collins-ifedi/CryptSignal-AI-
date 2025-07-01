from setuptools import setup, find_packages
import os

# Function to read the README.md file for the long description.
# It handles the case where README.md might not exist yet.
def read_readme():
    try:
        # Assumes README.md is in the same directory as setup.py
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "A comprehensive Crypto Trading Signal Generation and Analysis Suite. No README.md found."

setup(
    name='cryptsignal-suite',  # A unique name for your package
    version='0.1.0',           # The current version of your package
    author='Collins ifedi', # Replace with your name/team
    author_email='ifedicollinslinx@gmail.com', # Replace with your contact email
    description='A comprehensive Crypto Trading Signal Generation and Analysis Suite.',
    long_description=read_readme(), # Uses the function above to get README content
    long_description_content_type='text/markdown', # Specifies that long_description is in Markdown
    url=None, # Removed as the project is not hosted on GitHub or a public URL
    packages=find_packages(),  # Automatically finds all Python packages in your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha', # Indicating project is in early development
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8', # Specifies the minimum Python version required
    install_requires=[
        # List your project's external dependencies here.
        # These match the libraries in your requirements.txt file.
        'pandas',
        'numpy',
        'pandas_ta',
        'requests',
        'pyyaml',
        'beautifulsoup4',
        'fastapi', 
        'uvicorn', 
        'websockets',
    ],
    # You can define console scripts here if you want to make your main.py executable
    # directly via `pip install` (e.g., users can type `cryptsignal-main` in terminal)
    entry_points={
        'console_scripts': [
            'cryptsignal-main=main:main_menu', # 'main' is your main.py file, 'main_menu' is the function to run
        ],
    },
)