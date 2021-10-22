# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

a, b, c = map(int, input().split())

r1 = (a+b)%c
r2 = ((a%c)+(b%c))%c

r3 = (a*b)%c
r4 = ((a%c)*(b%c))%c

print(r1, r2, r3, r4)

# 같은 값을 가짐
