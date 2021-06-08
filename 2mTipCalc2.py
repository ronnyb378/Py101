#Goal: Calculate how much tip to leave a restaurant
# && rate the tip amount 

#input of bill & level of service 
bill = float(input('Total bill amount? '))
num = float(input('Split how many ways? '))
rating = float(input('Level of service between 1-10? '))
# good=20% / fair=15% / bad=10%
#calculates tip per service rating
if rating >= 7.75 :
    tip = .20 * bill
elif rating < 7.75 and rating > 5.0 :
    tip = .15 * bill
else:
    tip = .10 * bill

total = tip + bill 
#amount per person
per = total // num 

# Display tip/total/rating 
print('Bill amount: $', bill)
print('Tip amount: $', tip)
print('Total amount: $', tip+bill)
print('Amount per person: $', per)