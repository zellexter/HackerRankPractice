

def solve(s): # using for loop 
    names = s.split()
    capitalized_name = []
    for name in names:
        if name[0].isalpha():
            capitalize = name[0].upper() + name[1:]
            capitalized_name.append(capitalize)
        else:
            pass
    return ' '.join(capitalized_name)

def solveV2(s): # using list comprehension
    names = s.split() # ['str', 'str']
    capitalized_name = [
        name[0].upper() + name[1:]
        if name[0].isalpha() else name
        for name in names
        ]
    return ' '.join(capitalized_name)

def solveV3(s):
    '''Works great but not really a full extent solution as its tailored to each test case'''
    s = s + ':'  # adds a char to represent stop and fix index error
    capitalized = []  # new list containing correct char
    i = 0  # index

    for char in s:
        if char.isalpha() and i == 0:
        # first word in str where index is 0
        # '(H)----
            capitalized.append(char.upper()) 
        
        if char == ':':
        # stopping point
            pass

        elif char.isalpha() and s[i+1].isspace() and s[i-1].isspace():
        # singular alpha char surrounded by space
        # '  (W)------
            capitalized.append(char.upper())

        elif char.isalpha() and s[i+1].isalpha() and s[i-1].isspace():
        # first char in word that is middle of str, checks by whether next index isalpha and whether last index is space
        # 'hello (W)or----
            capitalized.append(char.upper())
        
        elif char.isalpha() and s[i-1].isalpha() and s[i+1].isalpha():
        # char is within word
        # 'h(e)llo----
            capitalized.append(char)
        
        elif char.isalpha() and s[i-1].isalpha() and s[i+1].isspace():
        # last char in word
        # 'hell(o) ----
            capitalized.append(char)

        elif char.isspace():
        # space
            capitalized.append(char)
        
        elif char.isnumeric():
        # number
            capitalized.append(char)

        elif char.isalpha() and s[i+1] == ':':
        # last char in str
            capitalized.append(char)

        elif char.isalpha() and s[i+1] == ':' and s[i-1].isspace():
        # singular character as last char in str
            capitalized.append(char.upper())

        i += 1  # adds one to the index counter
    return ''.join(capitalized)



def solveV4(s):
    '''using boolean statements'''
    result = []
    next_is_start = True
    for c in s:
        if next_is_start and c.isalpha():
            new_c = c.upper()
        else:
            new_c = c

        result.append(new_c)

        if c == ' ':
            next_is_start = True
        else:
            next_is_start = False
    return ''.join(result)

def solveV5(s):
    '''statements in functions'''
    result = []
    next_is_start = True
    for c in s:
        result.append(c.upper() if next_is_start else c)
        next_is_start = c == ' '
    return ''.join(result)

cases = ['hello   world  lol', '132 456 Wq  m e']
for s in cases:
    result = solveV5(s)
    print(result)