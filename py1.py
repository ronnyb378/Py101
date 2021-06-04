print('Hello World')

print('''Line 1
Line 2
Line 3''')

#always leave comments
#the following is done with 'Command-/'

# print('''Line 1
# Line 2
# Line 3''')

# a escape characters with '\'
print ('Hello \'the\' World')

# concatinate items with '+' 
print("Hello world" + " What's good")
print("The result of 1 + 1 is " + str(1+1))

# interger = whole number
print(1)

# float = fractional number
print(2.2)

# adding float + int
print(2.23 + 5)

#Python community uses snakecase (variables are spaced with underscore)
first_name = "Ronny"
print('Hello, ' + first_name)


try:
    first_num = 9 
    seconf_num = 23
    answer = first_num + seconf_num
    print(answer)

except:
    print('Oops something went wrong')
