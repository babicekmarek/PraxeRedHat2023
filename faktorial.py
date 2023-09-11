print("faktorial")

def faktorial(number):
    vysl = 1
    for x in range(1,number+1):
        vysl = vysl * x
    print("faktorial",number,"je",vysl)

faktorial(5)
