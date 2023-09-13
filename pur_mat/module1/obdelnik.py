from module1.matBase import MatBase

class Obdelnik(MatBase):
    def __init__(self, str1, str2):
        super().__init__(str1, str2)

    def obvod(self):
        return (2*self.str1)+(2*self.str2)

    def obsah(self):
        return self.str1 * self.str2
