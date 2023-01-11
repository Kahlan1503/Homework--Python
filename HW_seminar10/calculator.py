import re


def split(eq):
    return [i if i in "+-*/()^" else float(i) for i in re.findall("[0-9]+[.]*[0-9]*|[+\-*/]", eq)]


def multiplication(eq):
    for i, item in enumerate(eq):
        if item == "*":
            eq = eq[:i - 1] + multiplication([eq[i - 1] * eq[i + 1]] + eq[i + 2:])
            break
        if item == "/":
            eq = eq[:i - 1] + multiplication([eq[i - 1] / eq[i + 1]] + eq[i + 2:])
            break
    return eq


def summation(eq):
    for i, item in enumerate(eq):
        if item == "+":
            eq = eq[:i - 1] + summation([eq[i - 1] + eq[i + 1]] + eq[i + 2:])
            break
        if item == "-":
            eq = eq[:i - 1] + summation([eq[i - 1] - eq[i + 1]] + eq[i + 2:])
            break
    return eq


def calculate(eq):
    eq = multiplication(eq)
    eq = summation(eq)
    return eq