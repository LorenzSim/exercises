# Write your code here

def slug(string):
    words = ([w.lower() for w in string.split(' ')])
    first = words[0]
    rest = words[1:]
    rest.extend(first)
    return '-'.join(rest)
    
