import argparse
import re

def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("syntax", help="Filename of syntax file")
    parser.add_argument("theme", help="Filename of theme file")
    parser.add_argument("program", help="Filename of program to highlight")
    args = parser.parse_args()
    return args

def read_syntax_file(file):
    syntax = {}
    for line in file:
        line = line.split(':')
        size = len(line)
        regex = ""
        counter = 0
        while (size > 2):
            regex += line[counter]
            regex += ":"
            size -= 1
            counter += 1
        regex += line[counter]
        regex = regex[1:-1]
        name = line[counter + 1][1:]
        name = name.replace('\n', '')
        syntax[name] = regex
    return syntax

def read_theme_file(file):
    theme = {}
    for line in file:
        line = line.split(":")
        name = line[0]
        color = line[1]
        color = color.strip()
        color = color.replace("\n", "")
        theme[name] = color   
    return theme

def highlight(file, syntax, theme):
    program_str = file.read()    
    items = []
    for key in syntax.keys():
        regex = syntax[key]
        for item in re.finditer(regex, program_str): # item is a match object
            items.append((item.start(), item.end(), key))
    items.sort(key=lambda index: index[0]) 
    offset = 0
    for start, end, key in items:
        s = start + offset
        e = end + offset
        colored = "\33[" + theme[key] + "m" + program_str[s:e] + "\33[0m"
        program_str = program_str[:s] + colored + program_str[e:] # replace with colored
        offset += len(colored) - (e - s)
    return program_str

def main():
    args = handle_arguments()
    syntax_file = open(args.syntax, "r")
    theme_file = open(args.theme, "r")
    program_file = open(args.program, "r")   
    syntax = read_syntax_file(syntax_file)
    theme = read_theme_file(theme_file)   
    highlighted_file = highlight(program_file, syntax, theme)
    print(highlighted_file)

if __name__ == '__main__':
    main()
