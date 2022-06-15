#File dated ~ 10/XX/21
import random
# setup numbers.
# n1 is a * c
# n2 is b
# math stuff
n1 = input("Number one\n?")
n2 = input("Number two\n?")

n1 = int(n1)
n2 = int(n2)

#4 l8r
n2a = abs(n2)

b1 = 0
b2 = 0
ba = 0
bm = 0

# attempts
att = 0
b1 = n2a
while not ba == n2 or not bm == n1:
    
    #weird math thing here, sort of like a reverse absolute??
    #b1 = random.randint((n2a-(n2a*2)), n2a)
    b1 -= 1
    # to prevent div by 0 errors
    if not b1 == 0:
        att += 1
        b2 = n1 / b1
        ba = b1 + b2
        bm = b1 * b2
        if not ba == n2:
            print(att, "| FAILED", b1, ",", b2)
print(att, "| SUCCESS!")
print(b1, "+", b2, "=", b1 + b2)
print(b1, "*", b2, "=", b1 * b2)
# THIS WORKED SO WELL I LOVE IT
