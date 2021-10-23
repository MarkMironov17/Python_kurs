a = [57.08, 46.51, 97, 51.05, 35.56, 78.07, 43.89, 24.98, 63.73, 95.12]

q = int(a[0])
w = int(100 * (a[0] - q))
e = int(a[1])
r = int(100 * (a[1] - e))
t = int(a[2])
y = int(100 * (a[2] - t))
u = int(a[3])
i = int(100 * (a[3] - u))
o = int(a[4])
p = int(100 * (a[4] - o))
x = int(a[5])
s = int(100 * (a[5] - x))
d = int(a[6])
f = int(100 * (a[6] - d))
g = int(a[7])
h = int(100 * (a[7] - g))
j = int(a[8])
k = int(100 * (a[8] - j))
l = int(a[9])
z = int(100 * (a[9] - l))

print(f'{q} руб 0{w} коп, {e} руб {r} коп, {t} руб 0{y} коп, '
      f'{u} руб 0{i} коп, {o} руб {p} коп, {x} руб 0{s} коп, '
      f'{d} руб {f} коп, {g} руб {h} коп, {j} руб {k} коп, '
      f'{l} руб {z} коп')

a = sorted(a)
print(a)

b = sorted(a, reverse = True)
print(b)

v = b [:5]
print(v)