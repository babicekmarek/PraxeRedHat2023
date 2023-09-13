from module1 import ctverec
from module1 import obdelnik

if __name__ == "__main__":
    c=ctverec.Ctverec(5)
    print("ctverec")
    print("obvod:", c.obvod())
    print("obsah:", c.obsah())
    o=obdelnik.Obdelnik(4, 3)
    print("obdelnik")
    print("obvod:", o.obvod())
    print("obsah:", o.obsah())
