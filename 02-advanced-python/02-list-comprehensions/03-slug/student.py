# Write your code here

def slug(string):
    words = string.lower().split(" ")
    return '-'.join(words[1:] + [words[0]])
    
