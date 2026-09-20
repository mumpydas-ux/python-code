a = 25
b = 35
c = 45
avg = (a + b + c) / 3
if avg > a and avg > b and avg > c:
    print("higher than all three")
elif avg > a and avg > b:
    print("higher than a, b")
elif avg > a:
    print("just higher than a")
else:
    print("invalid input")