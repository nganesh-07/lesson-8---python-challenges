a = int(input("Enter your first value here:"))
b = int(input("Enter your second value here:"))
c = int(input("Enter your third value here:"))

avg = (a + b + c)/3
print("The average is", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg,a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > a:
    print("%d is higher than %d" %(avg, a))
elif avg > b:
    print("%d is higher than %d" %(avg, b))
elif avg > c:
    print("%d is higher than %d" %(avg, c))
else:
    print("invalid input.")