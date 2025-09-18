import os
import time
from errors import errors

digits = '0123456789'

def decode_file(file):
    boolean = {}
    operators = {
        '+': '+', 
        '-': '-', 
        '*': '*',
        '/': '/',
        '--': '//',
        '$': '%', 
        '<': '<', 
        '^': '**', 
        '>': '>',
        '=': '==',
        '->': '>=',
        '-<': '<=',
        'Pi': '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610453266482',
        'Π': '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610453266482',
        }
    for line in file:
        for token in line.split():
            if token in operators and not line.endswith("?") and not line.startswith("IF"):
                if line in digits or digits:
                    line = line.replace(token, f'{operators[token]}')
                    print(eval(line))
        if line.startswith("printStr"):
            print(line[9:].replace('<n>', '\n').replace('|>', '• ').replace('|*', '\033[1m').replace('*|', '\033[0m').replace('|I', '\x1B[3m').replace('|*U', '\x1B[4m').replace('S|', '\x1B[0m'))
        elif line.startswith("printBold"):
            print(f'\033[1m{line[10:]}\033[0m')
        elif line.startswith("title"):
            print(f'\033[1m{line[6:].upper()}\033[0m \n')
        elif line.startswith("italic"):
            print(f"\x1B[3m{line[7:]}\x1B[0m")
        elif line.startswith("underline"):
            print(f"\x1B[4m{line[10:]}\x1B[0m")
        elif line.startswith("wait"):
            time.sleep(float(line[5:]))
        elif line.startswith("gets"):
            answer = input(line[5:])
        elif line.startswith("getsS"):
            answer = input(line[6:])
            print("#=> " + answer)
        elif line.startswith("getsInt"):
            answer = int(input(line[8:]))
            print(f"#=> {answer}")
        elif line.startswith("IF"):
            tor = line[3:]
            eval(tor.replace('=', '==').replace('-<', '<=').replace('->', '>='))
            if tor:
                print("YYYYYYYYYYYYYYYYYYYYYYYYYYYY")
                nxt = next(file)
                decode_file(nxt)
        else:
            errors(line)

        
        


def decode(line):
    operators = {
        '+': '+', 
        '-': '-',
        '/=': '!=', 
        '*': '*',
        '/': '/',
        '--': '//',
        '$': '%', 
        '<': '<', 
        '^': '**', 
        '>': '>',
        '=': '==',
        '->': '>=',
        '-<': '<=',
        'Pi': '3.141592653589793',
        'Π': '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610453266482',
        }
    for token in line.split():
        if token in operators and not '<->' in line:
            if line in digits or digits:
                line = line.replace(token, f' {operators[token]}')
                print(eval(line))
        elif token == '<->':
            position = line.index(token)
            x = line[:position].strip().replace('/=', '!=').replace('=', '==').replace('-<', '<=').replace('->', '>=')
            y = line[position + 3:].strip()
            result: int = (x > y) - (x < y)
            print(result)
    if line.startswith("printStr"):
        print(line[9:].replace('<n>', '\n').replace('|>', '• ').replace('|*', '\033[1m').replace('*|', '\033[0m'))
    elif line.startswith("printBold"):
        print(f'\033[1m{line[10:]}\033[0m')
    elif line.startswith("title"):
        print(f'\033[1m{line[6:].upper()}\033[0m \n')
    elif line.startswith("italic"):
        print(f"\x1B[3m{line[7:]}\x1B[0m")
    elif line.startswith("underline"):
        print(f"\x1B[4m{line[10:]}\x1B[0m")
    elif line.startswith("wait"):
        time.sleep(int(line[5:]))
    elif line.startswith("gets"):
        answer = input(line[5:])
        print(f"#=> {answer}")
    else:
        errors(line)

os.system('cls' if os.name == 'nt' else 'clear')
print('---------------------------------')
print('Eureka!')
print('----------------------------------\n')
print('Type \'FILE <filename>\' to run an file.\nOtherwise type in commands directly and see their output.\n')
while True:
    command = input('Eureka! >>> ')
    if command[:4] == 'FILE':
        os.system('cls' if os.name == 'nt' else 'clear')
        with open(command[5:].strip(), 'r') as f:
            decode_file(f)
    elif command == '@exit':
        print('Exiting ...')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    elif command == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('---------------------------------')
        print('Eureka!')
        print('----------------------------------\n')
        print('Type \'FILE <filename>\' to run an file.\nOtherwise type in commands directly and see their output.\n')
    elif command == 'help':
        print('Commands:\nFILE <filename> - Runs a file\nclear - Clears the screen\n@exit - Exits the program\nhelp - Shows this message\nOther commands are in the \'turials\' folder.')
    else:
        decode(command)
