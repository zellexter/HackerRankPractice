import textwrap

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = int(4)

def wrap(string, max_width):
    line = []
    count = 0
    whole = []
    
    for i in range(0, len(string)):  
        line.append(string[i])
        count += 1
        if count == max_width:  
            whole.append(''.join(line))
            count = 0
            line = []

    if line:
        whole.append(''.join(line))

    return '\n'.join(whole)

def wrapV2(string, max_width):
    # trying with index slicing
    for i in len(string):
        section = string[:i]


result = wrap(string, max_width)
print(result)

