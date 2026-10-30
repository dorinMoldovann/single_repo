x = int(input("Enter a number: "))
X = x // 2
f = 0
for i in range(1, X):
    if x % i == 0:
        f += 1
        print(f'{f}. {i}')
print(f'{f + 1}. {x}')

