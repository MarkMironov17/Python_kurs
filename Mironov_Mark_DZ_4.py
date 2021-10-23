a = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

b = ''.join(str.lower(a[0]))
c = ''.join(str.lower(a[1]))
d = ''.join(str.lower(a[2]))
e = ''.join(str.lower(a[3]))

f = b.split()
q = c.split()
w = d.split()
t = e.split()

print(f'Привет, {str.capitalize(f[1])}!')
print(f'Привет, {str.capitalize(q[2])}!')
print(f'Привет, {str.capitalize(w[3])}!')
print(f'Привет, {str.capitalize(t[1])}!')

