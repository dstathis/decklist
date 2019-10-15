#!/usr/bin/python3

import scrython

def generate_data():
    with open('decklist/setcodes.py', 'w') as setfile:
        setfile.write('setcodes = {\n')
        sets = scrython.sets.Sets()
        for expansion in sets.data():
            setfile.write(f'    \"{expansion["code"]}\": \"{expansion["name"]}\",\n')
        setfile.write('}')


def main():
    generate_data()


if __name__ == '__main__':
    main()
