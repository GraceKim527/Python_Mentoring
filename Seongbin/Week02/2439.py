n = int(input( ))

for i in range(n):
    string = ''
    
    for j in range(n - 1 - i):
        string += ' '
    
    for j in range(i + 1):
        string += '*'
    
    print(string)
