# IMPROVEMENTS
# DONE print from list:
#   instead of giving instructions for top and bot of rangoli, generate list where elements in list represent lines of rangoli
#   [list comp to generate top of rangoli where loop stops when first/last element in str is abc != '-', list comp to generate bot of rangoli]

def print_rangoli(size):
    
    # reversed list of usable abc characters in rangoli
    abc = [chr(i) for i in range(97, 123)][:size]
    abc.reverse()
    len_abc = len(abc)
    
    # width of rangoli
    w = size + (size-1)
    w += (w-1)
    
    # top of rangoli
    for i in range(len_abc):
        # letters to print
        prin = abc[:i+1]
        # mirror
        # [::-1] where step is -1, reverses the whole list with no start/stop indicator
        prin = prin + prin[:-1][::-1]
        # joins prin with '-' as seperator and centers
        print('-'.join(prin).center(w, '-'))
        
    # bot of rangoli
    # len_abc - 1 because center line is already done by prev loop
    for i in range(len_abc-1):
        # letters to print
        prin = abc[:len(abc) - i - 1]
        # mirror
        # START:STOP:STEP prin[:-1] stops at the second to last element and [::-1] reverses the list
        prin = prin + prin[:-1][::-1]
        print('-'.join(prin).center(w, '-'))

def print_rangoli_LC(size):
    # reversed list of usable abc characters in rangoli
    abc = [chr(i) for i in range(97, 97+size)]
    abc.reverse()
    len_abc = len(abc)

    # width of rangoli
    w = size + (size-1)
    w += (w-1)

    # LC (what you want, from where to get data, condition)
    rangoli_top = [
        '-'.join(abc[:i+1] + abc[:i+1][:-1][::-1]).center(w, '-') 
        for i in range(len_abc) 
        ]
    rangoli_bot = [
        '-'.join(abc[:len(abc)-i-1] + abc[:len(abc)-i-1][:-1][::-1]).center(w, '-') 
        for i in range(len_abc-1)
        ]
    rangoli = rangoli_top + rangoli_bot
    
    for line in rangoli:
        print(line)

