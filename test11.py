def decorator(func):
    def inner():
        print('装饰器')
        return func()
    return inner


@decorator
class Aa:
    def qq(self):
        print('22222')









