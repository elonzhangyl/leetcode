class Bar:
    foo = 999
    def __init__(self) -> None:
        # self.foo = 1
        pass
    def lost(self):
        self.lll = 123

we = Bar()
we.lost()
print('123')