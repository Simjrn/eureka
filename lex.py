import os
import time

os.system('cls' if os.name == 'nt' else 'clear')
print("""###############################
Eureka!
###############################""")
print("version 1.5")
print("\n")

class Lex:

    def lexer(code):
        data = {}
        tokens = []
        operators = "-+/*$<^>:"  
        for line in code.strip().split('\n'):
            if line.startswith("//"):
                tokens.append("   ")
                tokens.append("   ")
                tokens.append("   ")
                continue
            for token in line.strip().split(' '):
                if ':' in line:
                    parts = line.split(':', 1)
                    variable_name = parts[0].strip()
                    expression = parts[1].strip()
                    data[variable_name] = expression
                    
                elif token == "printCalc":
                    tokens.append("PRINT NUMBERS")
                elif token == "printStr":
                    tokens.append("PRINT STRING")
                    tokens.append(line[9:])
                elif token == 'printVar':
                    tokens.append("PRINT VAR")
                elif token == "gets":
                    tokens.append("gets")
                    tokens.append(line[5:])
                    tokens.append(line[5:])
                elif token == 'wait':
                    print("hhh")
                    tokens.append("SLEEP: ")
                    tokens.append("  ")
                    del tokens[1]
                elif token == "Pi":
                    tokens.append("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482")
                    del tokens[-2]
                elif token in operators:
                    tokens.append(f"OPERATOR: {token}")
                elif token.isnumeric():
                    tokens.append(f"NUM: {token}")
                else: 
                    tokens.append(f"{token}")
        tokens.append("  ")
        tokens.append("  ")
        if tokens[0] == 'PRINT VAR':
            print(f"{data[variable_name]}")
        elif tokens[0] == 'PRINT STRING':
            printing = tokens[0:]
            print(printing[1])
        elif tokens[0] == 'PRINT NUMBERS' and len(tokens) == '2':
            print(tokens[1])
        elif tokens[:5] == "SLEEP":
            time.sleep(int(tokens[2][5:]))
        elif tokens == ['3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482']:
            print(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482)
        elif tokens[2][-1] == '*':
            print(int(tokens[1][5:]) * int(tokens[3][5:]))
        elif tokens[1][-1] == '*':
            return(int(tokens[0][5:]) * int(tokens[2][5:]))
        elif tokens[2][-1] == '/':
            print(int(tokens[1][5:]) / int(tokens[3][5:]))
        elif tokens[1][-1] == '/':
            return(int(tokens[0][5:]) / int(tokens[2][5:]))
        elif tokens[2][-1] == '-':
            print(int(tokens[1][5:]) - int(tokens[3][5:]))
        elif tokens[2][-1] == '-':
            return(int(tokens[1][5:]) - int(tokens[3][5:]))
        elif tokens[2][-1] == '+':
            print(int(tokens[1][5:]) + int(tokens[3][5:]))
        elif tokens[1][-1] == '+':
            return(int(tokens[0][5:]) + int(tokens[2][5:]))
        elif tokens[2][-1] == '$':
            print(int(tokens[1][5:]) % int(tokens[3][5:]))
        elif tokens[1][-1] == '$':
            return(int(tokens[0][5:]) % int(tokens[2][5:]))
        elif tokens[2][-1] == '<':
            print(int(tokens[1][5:]) < int(tokens[3][5:]))
        elif tokens[1][-1] == '<':
            return(int(tokens[0][5:]) < int(tokens[2][5:]))
        elif tokens[2][-1] == '^':
            print(int(tokens[1][5:]) ** int(tokens[3][5:]))
        elif tokens[2][-1] == '^':
            return(int(tokens[0][5:]) ** int(tokens[2][5:]))
        elif tokens[2][-1] == '>':
            print(int(tokens[1][5:]) > int(tokens[3][5:]))
        elif tokens[1][-1] == '>':
            return(int(tokens[0][5:]) > int(tokens[2][5:]))
        elif tokens[0] == "gets":
            answer = input(tokens[1] + '\n')
            print(f"#=> {answer}")
          

while True:
    code = input("Eureka >>> ")
    Lex.lexer(code)
