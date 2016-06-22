#3.2

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
if hrs <=40 :
 pay = h*r
else :
 pay = 40*r
 diff = h-40
 pay = pay + (diff*(r*1.5))
print pay