'''
Split a sentence into words
'''

def split(s: str):
    lst = ''
    cur = ''
    wrds = []
    w = ''
    for cur in s:
        if lst == ' ':
            wrds.append(w)
            w = ''
            
        if cur != ' ':
            w += cur
            
        lst = cur
        
    wrds.append(w)
            
    return(wrds)


if __name__ == '__main__':
    print(split('This is a sentence'))

    
            