from .a.aa import Aa
from .b.bb import Bb


class Abc:
    def __init__(self):
        self.abc = "abc"

    def abcmain(self):
        a = Aa()
        a.aaa()

        b = Bb()
        b.bbb()
