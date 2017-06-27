num=int(raw_input("enter a number to check wethear it is prime or not: "))
sign=0
for x in range(2,num-1):
    if num % x==0:
        sign=1

if sign==0:
    print "number is prime"

else:
    print "number is not prime"