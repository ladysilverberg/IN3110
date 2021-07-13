import argparse
import re
from highlighter import read_syntax_file, read_theme_file, highlight

def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("original", help="Original file")
    parser.add_argument("modified", help="Modified file")
    parser.add_argument("--color", action="store_true", help="colors the added and deleted lines")
    args = parser.parse_args()
    return args

def diff(og, mod, color):
    if color:
        f = open("demo.colordiff_espenlon.txt", "w+")
    
    mod_lines = []
    for line in mod:
        line = line[:-1]
        mod_lines.append(line)
    
    og_lines = []
    for line in og:
        line = line[:-1]
        og_lines.append(line)
    
    mod_index = 0
    og_index = 0
    
    while og_index < len(og_lines) or mod_index < len(mod_lines):
        mod_inc = 1
        og_inc = 1
        
        if og_index >= len(og_lines):
            if color:
                f.write("+" + mod_lines[mod_index] + "\n")
            else:
                print("+" + mod_lines[mod_index])
        elif mod_index >= len(mod_lines):
            if color:
                f.write("-" + og_lines[og_index] + "\n")
            else:
                print("-" + og_lines[og_index])
        else:
            if og_lines[og_index] == mod_lines[mod_index]:
                if color:
                    f.write("0" + og_lines[og_index] + "\n")
                else:    
                    print("0" + og_lines[og_index])
            elif og_index + 1 < len(og_lines) and og_lines[og_index + 1] == mod_lines[mod_index]:
                if color:
                    f.write("-" + og_lines[og_index] + "\n")
                    f.write("0" + mod_lines[mod_index] + "\n")
                    og_inc = 2
                else:    
                    print("-" + og_lines[og_index])
                    print("0" + mod_lines[mod_index])
                    og_inc = 2
            elif mod_index + 1 < len(mod_lines) and og_lines[og_index] == mod_lines[mod_index + 1]:
                if color:
                    f.write("+" + mod_lines[mod_index] + "\n")
                    f.write("0" + og_lines[og_index] + "\n")
                    mod_inc = 2
                else:    
                    print("+" + mod_lines[mod_index])
                    print("0" + og_lines[og_index])
                    mod_inc = 2
            else:
                if color:
                    f.write("-" + og_lines[og_index] + "\n")
                    f.write("+" + mod_lines[mod_index] + "\n")
                else:
                    print("-" + og_lines[og_index])
                    print("+" + mod_lines[mod_index])
        og_index += og_inc
        mod_index += mod_inc
    
    if color:
        f.close()
        syntax_file = open("diff.syntax", "r")
        theme_file = open("diff.theme", "r")
        program_file = open("demo.colordiff_espenlon.txt", "r")       
        syntax = read_syntax_file(syntax_file)
        theme = read_theme_file(theme_file)       
        highlighted_file = highlight(program_file, syntax, theme)
        print(highlighted_file)

def main():
    args = handle_arguments()
    og = open(args.original, "r")
    mod = open(args.modified, "r")
    diff(og, mod, args.color)

if __name__ == '__main__':
    main()
