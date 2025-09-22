a = [4, 1, 5, 9]  # 適当な数字
for x in a:
    print(x, x*10)

b = ['Red', 'Green', 'Yellow']
for x in b:
    print(x)

for i in range(len(a)):
    x = a[i]
    print(x, x*10)

for (i, x) in enumerate(b):
    print(f'{x:6} -> index = {i}')

