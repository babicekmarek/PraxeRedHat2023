from module1.matBase import MatBase

class Ctverec(MatBase):
    def __init__(self, str1, str2=None):
        super().__init__(str1, str2)

    def obvod(self):
        return 4*self.str1

    def obsah(self):
        return self.str1*self.str1
