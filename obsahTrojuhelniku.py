import math
def areaTriangle(a,b,c):
    obsah=math.sqrt(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))    
    return obsah

