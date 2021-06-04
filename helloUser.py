user_name = input('What is your name? ')
print('Hello, ' + user_name)

fav_num = input('What is your favorate number? ')

try: 
    if fav_num < 22 : 
        print('Yay')
    elif fav_num >= 22 :
        print('Nay')
except: 
    print('Oops')