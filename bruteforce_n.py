#File dated ~ 10/XX/21
import random
# setup numbers.
# m1 is a * c
# m2 is b
# math stuff
n1 = input("a = ?\n")
n2 = input("c = ?\n")
n3 = input("b = ?\n")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

m1 = n1*n2
m2 = n3

#4 l8r
m2a = abs(m2)

b1 = 0
b2 = 0
ba = 0
bm = 0

# attempts
att = 0
b1 = m2a
while not ba == m2 or not bm == m1:
    
    #weird math thing here, sort of like a reverse absolute??
    #b1 = random.randint((m2a-(m2a*2)), m2a)
    b1 -= 1
    # to prevent div by 0 errors
    if not b1 == 0:
        att += 1
        b2 = m1 / b1
        ba = b1 + b2
        bm = b1 * b2
        if not ba == m2:
            print(att, "| FAILED", b1, ",", b2)
print(att, "| SUCCESS!")
print(b1, "+", b2, "=", b1 + b2)
print(b1, "*", b2, "=", b1 * b2)
# THIS WORKED SO WELL I LOVE IT
