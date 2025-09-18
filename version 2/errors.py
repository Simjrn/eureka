digits = '0123456789'
operators = ['+', '-', '*', '/', '--', '$', '<', '^', '>', '=', '->', '-<', 'Pi', 'Π']

def errors(line):
    if not line.startswith("printStr") and not line.startswith("gets") and not line.startswith("gestS") and not line.startswith("gestInt") and not line.startswith("IF"):
        tokens = line.split(' ')
        if not tokens[0] in digits and not tokens[0] in operators:
            print("\033[31mUnknown command: ", tokens[0], "\033[0m")
        else:
            for token in tokens:
                if not token in digits and not token in operators:
                    print("\033[31mUnknown token: ", token, "\033[0m")
                else:
                    print("\033[31mBadly places token: ", token, "\033[0m")

errors("printTTTe hello?")
