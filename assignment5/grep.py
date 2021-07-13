import argparse
import re

def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--highlight", action="store_true", help="Highlight text flag")
    parser.add_argument("file", help="File to grep")
    parser.add_argument("regex", nargs="+", default=[], help="Regular expression")
    args = parser.parse_args()
    return args

def grep(file, regexes, highlight):
    for line in file:
        line = line[:-1]
        has_match = False
        items = []
        for color, regex in regexes:
            for item in re.finditer(regex, line):
                items.append((item.start(), item.end()))
            items.sort(key=lambda index: index[0])
            if len(items) > 0:
                has_match = True
                if highlight:
                    line = highlight_line(line, items, color)
            items = []
        if has_match:
            print(line)

def highlight_line(line, items, color):
    offset = 0
    for start, end in items:
        s = start + offset
        e = end + offset
        colored = "\33[" + str(color) + "m" + line[s:e] + "\33[0m"
        line = line[:s] + colored + line[e:]
        offset += len(colored) - (e - s)
    return line

def main():
    args = handle_arguments()
    args.regex = args.regex[0][1:-1].split(",")
    regexes = []
    color = 32
    for regex in args.regex: 
        regexes.append((color, regex))
        color += 1
        if color > 39:
            color = 32
    file = open(args.file, "r")
    grep(file, regexes, args.highlight)

if __name__ == '__main__':
    main()
