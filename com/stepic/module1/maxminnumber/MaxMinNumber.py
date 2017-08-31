_first = int(input())
_second = int(input())
_third = int(input())

_rest = None


def returnMaxOfTwo(first, second):
    if first >= second:
        return first
    else:
        return second


def returnMinOfTwo(first, second):
    if first <= second:
        return first
    else:
        return second


maximum = returnMaxOfTwo(_first, _second)
maximum = returnMaxOfTwo(maximum, _third)

minimum = returnMinOfTwo(_first, _second)
minimum = returnMinOfTwo(minimum, _third)

if _first == maximum:
    if _second == minimum:
        _rest = _third
    else:
        _rest = _second
elif _second == maximum:
    if _first == minimum:
        _rest = _third
    else:
        _rest = _first
else:
    if _first == minimum:
        _rest = _second
    else:
        _rest = _first


print(maximum)
print(minimum)
print(_rest)
