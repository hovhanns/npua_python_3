def hello():
    print('Hello, world!')

class MyClass:
    def __init__(self):
        print('MyClass.__init__')

    def my_method(self):
        print('MyClass.my_method')


if __name__ == '__main__':
    print('message from module.py')
    hello()