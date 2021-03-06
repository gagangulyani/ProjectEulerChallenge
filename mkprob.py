"""
This Script Creates Problem Directory along with
it's Solutions.md containing Link to Solution of that particular
problem in different languages.
"""

from os import mkdir
from os.path import join, isdir, isfile
from argparse import ArgumentParser, RawTextHelpFormatter
from textwrap import dedent


def border(func):
    def wrap(*args):
        print('='*50)
        print('\n')
        func(*args)
        print('\n')
        print('='*50)
    return wrap


@border
def create_dir(dir_path: str, sol_path: str, number: int) -> None:
    """
        This function creates Problem directory with
        Problem Number as suffix
    """
    mkdir(dir_path)
    print(f'Problem Directory "{dir_path}" Created!')

    create_solution(dir_path, sol_path, number)


@border
def create_markdown(path: str, number: int) -> None:
    """
        This function creates Solutions.md in Problem 
        Directory
    """
    markdown = f"# Problem #{number}\n\n\n"

    markdown_content = """
### Solutions
+ [Python](solution.py)
+ [Javascript](solution.js)
+ [C++](solution.cpp)

### Solutions [Optimized] [TODO]
+ [Python](solution_optimized.py)
+ [Javascript](solution_optimized.js)
+ [C++](solution_optimized.cpp)
    """
    if not isfile(path):
        with open(path, 'w') as f:
            f.write(markdown)
            f.write(markdown_content)
            print('"Solutions.md" Created!')
    else:
        print('"Solutions.md" Already Exists!')


@border
def create_solution(dir_path: str, sol_path: str, number: int) -> None:
    """
        This function creates Solution boilerplate
        consisting of Program files and then calls
        create_markdown() for Creating Solution 
        Markdown file for Navigating each Solution
        with ease
    """
    extensions = ['js', 'py', 'cpp']

    for ext in extensions:

        # Program file name with Path
        scr_name = join(dir_path, f'solution.{ext}')
        scr_name2 = join(dir_path, f'solution_optimized.{ext}')

        if isfile(scr_name):
            # If file exists, then don't touch it
            print(f'"solution.{ext}" Already Exists!')
        else:
            # Else Create File
            open(scr_name, 'w').close()
            print(f'"solution.{ext}" Created!')

        if isfile(scr_name2):
            # If file exists, then don't touch it
            print(f'"solution_optimized.{ext}" Already Exists!')
        else:
            open(scr_name2, 'w').close()
            print(f'"solution_optimized.{ext}" Created!')

    create_markdown(sol_path, number)
    print(f'Solution Boilerplate for Problem {number} Created!')


# Creating Argument Parser object
parser = ArgumentParser(
    description=dedent('''
Creates Directory or Directories with Problem Number(s) as Suffix and adds 
Solutions Boilerplate consisting of Solutions.md, solution.js, solution.py and 
solution.cpp.
        '''),
    usage="%(prog)s [options] problem_number",
    prog='mkprob.py',
    formatter_class=RawTextHelpFormatter,
    epilog=dedent("""
Example Usage:
  Usage #1: Creating One Problem Directory
    mkprob.py 17
  
  Usage #2: Creating Multiple Problem Directories
    mkprob.py 17 18 19 20
""")
)

# Version Number of the Script
parser.version = '0.1'

# Positional Argument for Problem Number
parser.add_argument(
    'problem_number',
    metavar='problem_number',
    type=int,
    help='Creates Directory or Directories with Problem Number(s) as suffix',
    action='store', nargs='+'
)

# Optional Agument for Version Number
parser.add_argument('-v', '--version', action='version')

# Parse Aruguments
args = parser.parse_args()
numbers = list(set(args.problem_number))

for number in numbers:

    # File Names
    dir_name = f'Problem {number}'
    sol_file_name = 'Solutions.md'

    # Path to Solutions.md
    sol_path = join(dir_name, sol_file_name)

    prompt = True

    if isdir(dir_name):
        print(f'\nDirectory "{dir_name}" Already Exists...')
        create_solution(dir_name, sol_path, number)

    else:
        print("\n")
        create_dir(dir_name, sol_path, number)

print('\nExiting..')
