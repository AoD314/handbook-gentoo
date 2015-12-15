#!/usr/bin/env python3.4

import sys

def get_answer(d):
    answers = []
    is_corrent = False
    while not is_corrent:
        answers = []
        for q in d:
            print("Enter " + q + ": ", end='')
            sys.stdout.flush()
            answers.append(input())

        max_len_q = max([len(e) for e in d])
        print("\nresults:")
        for i, q in enumerate(d):
            format_str = "{:>%ds} : [{}]" % max_len_q
            print (format_str.format(q, answers[i]))

        a = '?'
        while a not in ['y', 'n', 'q']:
            print("\nall answers are correct?(y/n/q): ", end='')
            a = input()
        print('')
        if a == 'y':
            is_corrent = True
        elif a == 'q':
            raise Exception('exit from question')

    return answers

def main():
    name, email = get_answer(['user name', 'e-mail'])
    print (name, email)

if __name__ == "__main__":
    main()