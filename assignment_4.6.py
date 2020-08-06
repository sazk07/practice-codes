def computepay(h,r):
    if h <=40:
       p = h*r
       return p
    else :
        h2 = h - 40
        r2 = r*1.5
        p = (40*r) + (h2*r2)
        return p 

hrs = input("Enter Hours:")
rate = input ("Enter rate: ")
h = float (hrs)
r = float (rate)

print("Pay",computepay(h,r))