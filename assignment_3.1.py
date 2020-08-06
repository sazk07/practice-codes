hrs = input ('Enter Hours: ')
h = float(hrs)

r = input ('Enter Rate: ')
rate = float (r)
if h <=40:
    pay = h*rate
    
    
else:
    h2 = h - 40
    rate2 = rate*1.5
    pay = (40*rate)+(h2*rate2)
print (pay)