"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic.py import *

def consume_input(entry):
    list1 = entry.split(" ")
    return list1


def evaluate(list2):
    operator = list2[0]
    v_1 = int(list2[1])
    v_2 = int(list2[2])
    if operator == "+":
        return add(v_1, v_2)
    elif operator == "-":
        return subtract(v_1, v_2)
    elif operator == "*":
        return multiply(v_1, v_2)
    elif operator == "/":
        return divide(v_1, v_2)
    elif operator == "square":
        return square(v_1)
    elif operator == "cube":
        return cube(v_1)
    elif operator == "pow":
        return power(v_1, v_2)
    elif operator == "mod":
        return mod(v_1, v_2)
    else:
        return "I don't understand!"


def main():
    string = raw_input("> ")
    split_string = consume_input(string)
    output = evalulate(split_string)
    print output

if __name__ == '__main__':
    main()
