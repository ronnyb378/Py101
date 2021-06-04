name = input('Name: ')
subject = input('Subject: ')

#*variable* = f"{variable} # this will swap out the variable
#with watever variable is swapping it out for it
story = f"{name} will go and {subject}."
#f in f'{variable}' is for

#OR

#string interpolation
story = "%s will go and %s. %d %.2f" % (name, subject, 10.9879, 5.194080234)
print(story)

