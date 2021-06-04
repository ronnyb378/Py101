# Day of the Week
day = int(input('Day 0-6? '))
try:
    if day == 0 :
        print('Sunday')
        print('Sleep in')
    elif day == 1 :
        print('Monday')
        print('Go to work')
    elif day == 2 :
        print('Tuesday')
        print('Go to work')
    elif day == 3 :
        print('Wednsday')
        print('Go to work')
    elif day == 4 :
        print('Thursday')
        print('Go to work')
    elif day == 5 :
        print('Friday')
        print('Go to work')
    else:
        print('Saturday')
        print('Sleep in')



except:
    print('Oops')