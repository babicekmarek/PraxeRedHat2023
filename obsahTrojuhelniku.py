import math
def areaTriangle(a,b,c):
    if a+b>c and b+c> and a+c>b:
        return math.sqrt(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c)) 
    else:
        return None

