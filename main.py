#НОМЕР 1
film = input()
cinema = input()
time = input()

print(f'Билет на «{film}» в «{cinema}» на {time} забронирован.')

#НОМЕР 2
stringa1 = input()
stringa2 = input()

if stringa1 in ("да", "нет") and stringa2 in ("да", "нет"):
    print("ВЕРНО")
else:
    print("НЕВЕРНО")

#НОМЕР 3
login = input()
email = input()

if "@" not in login and "@" in email:
    print("OK")
else:
    print("ERROR")

#НОМЕР 4
count = 0
heights = []

while True:
    s = input()
    if s == "!":
        break
    h = int(s)
    if 150 <= h <= 190:
        heights.append(h)
        count += 1

print(count)
print(min(heights), max(heights))

#НОМЕР 5
while True:
    p1 = input()
    p2 = input()

    if len(p1) < 8:
        print("Короткий!")
    elif "123" in p1:
        print("Простой!")
    elif p1 != p2:
        print("Различаются.")
    else:
        print("OK")
        break

#НОМЕР 6
n = int(input())

for i in range(n):
    print("*" * (2 * i + 1))

#НОМЕР 7
n = int(input())

num = 1
row = 1

while num <= n:
    for _ in range(row):
        if num > n:
            break
        print(num, end=" ")
        num += 1
    print()
    row += 1

#НОМЕР 8
s = input()

print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

#НОМЕР 9
s = input()

if "f" in s:
    if s.count("f") == 1:
        print(s.index("f"))
    else:
        print(s.index("f"), s.rindex("f"))

#НОМЕР 10
prev = input()

while True:
    word = input()
    if word[0] != prev[-1]:
        print(word)
        break
    prev = word

#НОМЕР 11
s = input()

for i, c in enumerate(s, start=1):
    print(c * i, end="")

#НОМЕР 12
path = input()

x = y = 0
points = [(x, y)]

for c in path[1:]:
    if c == ">":
        x += 1
    elif c == "<":
        x -= 1
    elif c == "V":
        y += 1
    points.append((x, y))

min_x = min(p[0] for p in points)

points = [(x - min_x, y) for x, y in points]

max_x = max(p[0] for p in points)
max_y = max(p[1] for p in points)

grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for x, y in points:
    grid[y][x] = path[0]

for row in grid:
    print("".join(row))

#НОМЕР 13
a = list(map(int, input().split()))

for i in range(1, len(a)):
    if a[i] > a[i-1]:
        print(a[i], end=" ")

#НОМЕР 14
a = list(map(int, input().split()))

for i in range(0, len(a)-1, 2):
    a[i], a[i+1] = a[i+1], a[i]

print(*a)

#НОМЕР 15
data = input().split()
indexes = list(map(int, data[:-1]))
words = data[-1:]

sentence = input().split()

result = [sentence[i-1] for i in indexes]

result[0] = result[0].capitalize()

print(" ".join(result))

#НОМЕР 16
print(len(set(map(int, input().split()))))

#НОМЕР 17
print(len(set(map(int, input().split())) & set(map(int, input().split()))))

#НОМЕР 18
n = int(input())
words = set()

for _ in range(n):
    words.update(input().split())

print(len(words))

#НОМЕР 19
words = input().split()

seen = {}

for w in words:
    print(seen.get(w, 0), end=" ")
    seen[w] = seen.get(w, 0) + 1

#НОМЕР 20
n = int(input())

d = {}

for _ in range(n):
    a, b = input().split()
    d[a] = b
    d[b] = a

word = input()

print(d[word])

#НОМЕР 21
n = int(input())

votes = {}

for _ in range(n):
    name, v = input().split()
    votes[name] = votes.get(name, 0) + int(v)

for name in sorted(votes):
    print(name, votes[name])

#НОМЕР 22
#1
[x for x in my_list if x < 5]

#2
[x / 2 for x in my_list]

#3
[x * 2 for x in my_list if x > 17]

#4
n = int(input())
squares = [i**2 for i in range(n+1)]

#5
nums = [int(x) for x in input().split()]
print(*[x**2 for x in nums])

#6
print(*[x**2 for x in map(int, input().split()) if x % 2 and (x**2) % 10 != 9])

#НОМЕР 23
nums = list(map(int, input().split()))

for n in nums:
    print("*" * n)

#НОМЕР 24
def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Это треугольник")
    else:
        print("Это не треугольник")

#НОМЕР 25
def palindrome(s):
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"