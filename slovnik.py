dict1 = {
  "price": 50,
  "size": 34,
  "year": 1964
}

for x in dict1.items():
    for y in x:
        if type(y) == int and  y < 100:
            print(x) 
