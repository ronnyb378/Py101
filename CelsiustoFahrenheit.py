#Celsius to Fahrenheit
try:
    C = input('Temperature in C? ')
    F = ((float(C) * 9/5) + 32)
    print(str(F) + ' F')
except: 
    print('Oops, try doing a number')