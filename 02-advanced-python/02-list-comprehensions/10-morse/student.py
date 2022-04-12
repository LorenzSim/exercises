# Write your code here

morse = {
    'A' : '.-',
    'B' :'-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..'
}
def to_morse(string):
    def word_to_morse(word): return ' '.join(morse[s.upper()] for s in word)
    return '   '.join(word_to_morse(word) for word in string.split(' '))

def from_morse(string):
    def to_letter(m): 
        for letter in morse.keys():
             if morse[letter] == m:
                 return letter
        return ''
    def to_word(m): return ''.join(to_letter(s) for s in m.split(' '))
    return ' '.join(to_word(s) for s in string.split('   '))