import re


def f1(a, b=0):
    return a**2 + b


def f2(param):
    if not param:
        return "BUUUUM"
    else:
        return param[0]


def f3(param):
    if param == 1:
        return "jeden"
    elif param == 2:
        return "dwa"
    elif param == 3:
        return "trzy"
    else:
        return "other"


def f4(text1, text2=None):
    text = text1 + " ma kota"

    if text2:
        text += " i " + text2

    return text


def f5(stop, step=1):
    return list(range(0, stop, step))


def f6(count, char):
    return char * count


def f7(param):
    if isinstance(param, str):
        exp = re.compile(r'\s')

        if exp.search(param):
            return "zdanie"

        startTagExp = re.compile(r'<\w+>')

        if startTagExp.search(param):
            return "tag poczatkowy"

        endTagExp = re.compile(r'</\w+>')

        if endTagExp.search(param):
            return "tag koncowy"

        return "slowo"
    else:
        if param >= 0 and param <= 9:
            return "cyfra"

        if param < 0:
            return "liczba_ze_znakiem"

        return "liczba"


def f8(pattern, search):
    return pattern in search


def f9(a, b):
    if a > 0 and b > 0:
        return "dodatnie"
    elif a < 0 and b < 0:
        return "ujemne"
    elif a == 0 or b == 0:
        return "jest zero"
    else:
        return "roznych znakow"


def f10(a, b):
    if a == b:
        return "rowne"
    else:
        return "rozne"