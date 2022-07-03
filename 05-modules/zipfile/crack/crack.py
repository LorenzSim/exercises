from zipfile import ZipFile
lower = 'abcdefghijklmnopqrstuvwxyz'

def generate_passwords():
    passwords = list()
    for char1 in lower:
        for char2 in lower:
            for char3 in lower:
                for char4 in lower:
                    passwords.append(f'{char1}{char2}{char3}{char4}'.encode(encoding='ascii'))
    return passwords



with ZipFile('crack.zip', 'r') as input:
    for passw in generate_passwords():
        try:
            print(input.read('file.txt', pwd=passw).decode())
            print(f'Password is: {passw.decode()}')
            break
        except: continue

