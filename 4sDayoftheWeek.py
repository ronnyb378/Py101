# Day of the Week
day = int(input('Day 0-6? '))
try:
    if day == 0 :
        print('Sunday')
        
    elif day == 1 :
        print('Monday')
        
    elif day == 2 :
        print('Tuesday')
        
    elif day == 3 :
        print('Wednsday')
        
    elif day == 4 :
        print('Thursday')
        
    elif day == 5 :
        print('Friday')
        
    else:
        print('Saturday')
        


except:
    print('Oops')