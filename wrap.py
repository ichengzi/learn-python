def makeitalic(func):
    def wrapped():
        print "<i>" + func() + "</i>"
    return wrapped

def hello():
    return 'hello world'

hello = makeitalic(hello)

hello()