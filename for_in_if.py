#!/usr/bin/env python

def main():
    li_with_seven = [3,5,7]
    li_no_seven   = [1,4,6]

    # this is called a list comprehension, you should read more about this
    print [el for el in li_with_seven if (el%7 == 0)]
    print [el for el in li_no_seven   if (el%7 == 0)]

    if len([el for el in li_with_seven if (el%7 == 0)]):
        print "seven in list"

    # seven not in list, won't print
    if len([el for el in li_no_seven if (el%7 == 0)]):
        print "seven in list"

if __name__ in '__main__':
    main()
