class soubor:
    def __init__(self, file:str):
        self.file = file

    def otevrit(self) -> str:
        with open(self.file, encoding="utf-8") as soubor:
            obsah = soubor.read()
        return obsah

file =  soubor ("file.txt")
print(file.otevrit())
