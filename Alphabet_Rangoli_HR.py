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

for x in range(1,27):
    print(f'RANGOLI SIZE {x}')
    print_rangoli(x)
    print()