#! python

import datetime
import re
from html.parser import HTMLParser
from subprocess import call
from sys import argv
from urllib.request import urlopen

# controls print statements containing input/output file contents for each case
DEBUG = True

class CodeforcesSingleProblemParser(HTMLParser):
    def __init__(self, problem, letter):
        HTMLParser.__init__(self)
        self.problem = problem
        self.letter = letter
        self.case_counter = 0
        self.case_file = None
        self.case_type = None
        self.start_copy = False
        self.end_line = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            if attrs == [('class', 'input')]:
                self.case_counter += 1
                self.case_type = 'in'
                self.case_file = open(f'{self.case_counter}.{self.case_type}', 'w')

            elif attrs == [('class', 'output')]:
                self.case_type = 'out'
                self.case_file = open(f'{self.case_counter}.{self.case_type}', 'w')

        elif tag == 'pre':
            if self.case_file is not None:
                self.start_copy = True

    def handle_endtag(self, tag):
        if tag == 'br':
            if self.start_copy:
                self.case_file.write('\n')
                self.end_line = False

        if tag == 'pre':
            if self.start_copy:
                if self.end_line:
                    self.case_file.write('\n')

                self.case_file.close()
                self.case_file = None
                self.start_copy = False

    def handle_entityref(self, name):
        if self.start_copy:
            self.case_file.write(self.unescape(f'&{name};'))

    def handle_data(self, data):
        if self.start_copy:
            clean_data = data.strip() + '\n'
            if DEBUG:
                case_line = f'Case {self.case_counter} : {self.case_type}'
                print('-' * len(case_line))
                print(case_line)
                print('=' * len(case_line))
                print(clean_data)
                print('-' * len(case_line))
                print('\n')
            self.case_file.write(clean_data)
            self.end_line = False


def parse_single_problem(problem, letter):
    url = f'http://codeforces.com/problemset/problem/{problem}/{letter}'
    print(f'url: {url}')
    html = urlopen(url).read()
    parser = CodeforcesSingleProblemParser(problem, letter)
    parser.feed(html.decode('utf-8'))
    return parser.case_counter


def main():
    if(len(argv) < 3):
        print('USAGE: ./<this_script>.py <problem_number_part> <problem_letter_part>')
        exit(1)

    target = f'{argv[1]}{argv[2]}.py'
    x = parse_single_problem(argv[1], argv[2])


if __name__ == '__main__':
    main()
