
def reverseText(text): 
    list = []

    for i in text:
        list.append(i)
        
    list.reverse()
    text = "".join(list)
    return text


