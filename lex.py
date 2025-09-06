print("""###############################
Eureka!
###############################""")

class Lex:

    def lexer(code):
        tokens = []
        operators = "-+/*$<>:"
        for line in code.strip().split('\n'):
             for token in line.strip().split(' '):
                if token == "printNum":
                    tokens.append("PRINT")
                elif token in operators:
                    tokens.append(f"OPERATOR: {token}")
                elif token.isnumeric:
                    tokens.append(f"NUM: {token}")
                else:
                    tokens.append("OTHER")
             tokens.append("---")    
        print(tokens)

while True:
    code = input("Eureka >>>")
    Lex.lexer(code)
