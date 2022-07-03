with open('output.txt', 'w').write() as output: 
    output.write('\n'.join(str(i) for i in range(1, 1000001)))