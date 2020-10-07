def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class MyException(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except MyException:
            print("Ops")
            break
        else:
            print("******************", message)
    return "AAAAAAAAAAAAAAAAAAAAAAA"


def print():
    for i in "Python":
        yield i


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except MyException as e:
    #         g.throw(e)
    res = yield from g
    print(res)


d = delegator(subgen())
