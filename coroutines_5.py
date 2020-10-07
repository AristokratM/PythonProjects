def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class MyException(Exception):
    pass


@coroutine
def average():
    count = 0
    x = 0
    avg = None
    while True:
        try:
            a = yield
        except StopIteration:
            print("Done")
            break
        except MyException:
            print("QQQQQQQQQQQQQQQ")
            break
        else:
            count += 1
            x += a
            avg = round(x / count, 2)
    return avg


@coroutine
def message():
    x = yield
    print("Message: " + x)


b = average()
m = message()

