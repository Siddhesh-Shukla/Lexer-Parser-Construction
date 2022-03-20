# TEAM MEMBERS:
    # Mudit Sharma 2019A7PS1344H
    # Siddhesh Shukla 2019A7PS0099H
    # Rahul Vegesna 2019A7PS1205H
    # Parth Gedia 2019A7PS0151H

RELATIONALOPERATOR = ['<','>','=','!']
DIGITS = '0123456789'
CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

KEYWORDS = ['if', 'elif', 'else', 'break', 'continue',          # conditional related keywords
            'switch', 'default', '$',                           # switch related keywords
            'int', 'char', 'float', 'void', 'array', 'string',  # datatype related ketwords
            'for', 'while',                                     # loop related keywords
            'function', 'begin', 'return',                      # function related keywords
            'print', 'println' 'input']                         # i/p - o/p related keywords

# read code
file = open('example.txt', 'r')
data = file.read()

# initializing index and line no.
idx = 0
line_no = 1

# iterating in input code
while idx < len(data):        
    
    if not data[idx]:
        break
    
    # Eliminating space
    if data[idx] == ' ':
        idx += 1
        continue

    # Incrementing line_no on new line
    elif data[idx] == '\n':
        line_no += 1

    # Eliminating comments
    elif data[idx] == '#':
        while idx < len(data) and data[idx] != '\n':
            idx += 1
        line_no += 1
    

    # Identifying digits
    elif data[idx] in (DIGITS + '.'):          
        num_str = ''
        dot_count = 0
        while idx < len(data) and data[idx] and (data[idx] in (DIGITS + '.')):
            if data[idx] == '.':
                dot_count += 1
                num_str += '.'
            else:
                num_str += data[idx]
            idx += 1
        if(data[idx] in CHARACTERS):
            while idx < len(data) and data[idx] in CHARACTERS:
                idx += 1
            print("Illegal Expression at line " + str(line_no))
        elif idx < len(data):
            if dot_count == 0:
                print("Integer " + num_str + " at line "+ str(line_no))
            elif dot_count == 1:
                print("Float "+ num_str + " at line "+ str(line_no))
            else:
                print("Illegal Representation of Floating Point Number (can't have more than 1 Decimal Point Places)")
        idx -= 1
    

    # Identifying Keywords & Identifiers
    elif data[idx] in CHARACTERS:
        var_str = ''

        while idx < len(data) and data[idx] != None and data[idx] in CHARACTERS + DIGITS + '_':
            var_str += data[idx]
            idx += 1
        
        if(var_str in KEYWORDS):
            print("Keyword "+ var_str + " at line " + str(line_no))
        else:
            print("Identifier " + var_str + " at line " + str(line_no))
        idx -= 1
    

    # Identifying Assignment Operator
    elif data[idx] == '=' and idx+1 < len(data) and data[idx+1] != '=':
        print("Assignment Operator at line " + str(line_no))
        idx += 1
        continue
    

    # Identifying String
    elif data[idx] == '"':
        start_line = line_no
        idx += 1
        while idx < len(data) and data[idx] and data[idx] != '"':
            if data[idx] == '\n':
                line_no += 1
            elif data[idx] == '\\':
                if idx+1 < len(data):
                    if data[idx+1] in ['\\', 'n', 't', 'r']:
                        idx += 1
                    else:
                        print("warning: unknown escape sequence at line: " + str(line_no))
                else:
                    print("warning: unknown escape sequence at line: " + str(line_no))
            idx += 1
        if idx >= len(data):
            print("ERROR: missing closing string delimiter")
        else:
            idx += 1
            print("String from line: " + str(start_line) + " to " + str(line_no))
    

    # Identifying Character
    elif data[idx] == "'":
        if idx+2 < len(data) and data[idx+2] == "'":
            print("Character '" + data[idx+1] + "' at line " + str(line_no))
            idx += 2
        else:
            print("ERROR: missing closing char delimiter")

    
    # Identifying Relational and Logical Operators
    elif data[idx] in RELATIONALOPERATOR:
        if data[idx] == '>' and idx+1 < len(data) and data[idx+1] == '=':
            print("Greater Than Equal to Operator at line " + str(line_no))
            idx += 1
        elif data[idx] == '>':
            print("Greater Than Operator at line " + str(line_no))
        elif data[idx] == '<' and idx+1 < len(data) and data[idx+1] == '=':
            print("Less Than Equal to Operator at line " + str(line_no))
            idx += 1
        elif data[idx] == '<':
            print("Less Than Operator at line " + str(line_no))
        elif data[idx] == '=' and idx+1 < len(data) and data[idx+1] == '=':
            print("Equal to Operator == at line " + str(line_no))
            idx += 1
        elif data[idx] == '!' and idx+1 < len(data) and data[idx+1] == '=':
            print("Not Equal Operator at line " + str(line_no))
            idx += 1
        elif data[idx] == '!':
            print("Not Operator at line " + str(line_no))
    elif data[idx] == '&' and idx+1 < len(data) and data[idx+1] == '&':
        print("And Operator at line " + str(line_no))
        idx += 1
    elif data[idx] == '|' and idx+1 < len(data) and data[idx+1] == '|':
        print("And Operator at line " + str(line_no))
        idx += 1
    

    # Identifying Mathematical Operators
    elif data[idx] == '+':
        print("Plus Operator " + "at line " + str(line_no))
    elif data[idx] == '-':
        print("Minus Operator " + "at line " + str(line_no))
    elif data[idx] == '*' and (idx+1 < len(data) and data[idx+1] == '*'):
        print("Exponent Operator " + "at line " + str(line_no)) 
    elif data[idx] == '*':
        print("Multiplication Operator " + "at line " + str(line_no))
    elif data[idx] == '/':
        print("Division Operator " + "at line " + str(line_no))
    elif data[idx] == '%':
        print("Modulus Operator " + "at line " + str(line_no)) 


    # Identifying Parenthesis
    elif data[idx] == '(':
        print("Left Parenthesis " + "at line " + str(line_no))
    elif data[idx] == ')':
        print("Right Parenthesis " + "at line " + str(line_no))
    elif data[idx] == '}':
        print("Right Curly Bracket " + "at line " + str(line_no))
    elif data[idx] == '{':
        print("Left Curly Bracket " + "at line " + str(line_no))
    elif data[idx] == '[':
        print("Left Square Parenthesis " + "at line " + str(line_no))
    elif data[idx] == ']':
        print("Right Square Parenthesis " + "at line " + str(line_no))
    
    
    # Identifying Seperators
    elif data[idx] == ',':
        print("Comma at line " + str(line_no))
    elif data[idx] == ';':
        print("Semicolon " + "at line " + str(line_no))
    

    # If no token matches
    else:
        print("ERROR: Illegal Operator used " + "at line " + str(line_no))
    
    
    # Incrementing index value
    idx += 1


# Closing file after reading 
file.close()