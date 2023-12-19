ma = 758
mb = 758
a = min(ma, mb)
print(a)
b = max(ma, mb)
print(b)
while b % a != 0:
    a = b % a
print(a)
