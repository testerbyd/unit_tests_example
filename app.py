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
    pass