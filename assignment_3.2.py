hrs = input ('Enter Hours: ')
r = input ('Enter Rate: ')
try:
    h = float(hrs)  
    rate = float (r)
except:
    print ('please enter numeric input')
    quit()
if h <=40:
    pay = h*rate
    
    
else:
    h2 = h - 40
    rate2 = rate*1.5
    pay = (40*rate)+(h2*rate2)
print (pay)