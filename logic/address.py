class Address:
    def __init__(self, decimal, binary, tag, index, offset):
        self.decimal = decimal
        self.binary = binary
        self.tag = tag
        self.index = index
        self.offset = offset

    def __tuple__(self):
        return (self.decimal, self.binary, self.tag, self.index, self.offset)
