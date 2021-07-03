"""
py -m pip install -U sphinx
create src and docs folders and open docs in the Terminal
run sphinx-quickstart
.\make.bat html
create your install.rst
add install to the table of contents in index.rst

1. Make a Python file with some documentation strings
2. py -m pip install sphinx-autoapi
3. Add these two lines to your conf.py

extensions.append('autoapi.extension')
autoapi_dirs = ['../src']

class Application:
    """this class is very useful because it does so many things"""
    def function1(self, name):
        """this function does something"""
        pass

    def function2(self):
        """this other function does something else"""
        pass

if __name__ == '__main__':
    my_app = Application()
    my_app.function1("nick")
    my_app.function2()