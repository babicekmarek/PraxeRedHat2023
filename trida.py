class soubor:
    def __init__(self, file:str):
        self.file = file

    def otevrit(self) -> str:
<<<<<<< HEAD
                with open(self.file, encoding="utf-8") as soubor:
                    obsah = soubor.read()
                return obsah
=======
        with open(self.file, encoding="utf-8") as soubor:
            obsah = soubor.read()
        return obsah
>>>>>>> 5726144e515acd2b6b8408decd75bd2250d37715

file =  soubor ("file.txt")
print(file.otevrit())
