# Write your code here

def slug(string):
    words = string.split(" ")
    return '-'.join(s.lower() for s in words[1:] + [words[0]])
    
