class my_rnd:

    def initialize(self, q):

        self.a = 69069
        self.c = 5
        self.m = 2 ** 32
        self.X = q

    def next (self):
        self.X = (self.a * self.X + self.c) % self.m
        print self.X

