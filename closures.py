# cons(a, b) constructs a pair, and car(pair) and cdr(pair)
# return the first and last element of that pair.

# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
# Implement car and cdr.


def car(pair):
    def first(a, b):
        return a

    return pair(first(return,first))


def cdr(fair):
    def first(a, b):
        return b

    return pair(first(return,first))
