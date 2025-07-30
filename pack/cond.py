x = 20
y = 40

# One condition
if x < y:
    print("x is less than y")

# Multiple conditions
if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is greater than y")

if x < y:
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")

if x == y and x + y == 60 or x - y == 0:
    print("Conditions met")

if (x == y and x + y == 60) or x - y == 0:
    print("Conditions met")

if x == y and (x + y == 60 or x - y == 0):
    print("Conditions met")


    