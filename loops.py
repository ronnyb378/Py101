

donuts_eaten=1 

while donuts_eaten <= 10:
    print(f'you have eaten {donuts_eaten} donuts.')
    donuts_eaten = donuts_eaten + 1


while True:
    print('working...')
    user_input = input('Should I stop? (y/n) ')
    if user_input == 'y':
        print('Thank You')
        exit()
    
    else: 
        print('sigh...')

print('finish')