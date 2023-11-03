# fungsi mencari bilangan Prima
def bilangan_prima(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Array / List kosong
angka = []

# Menambahkan isi list angka
for i in range(100, 0, -1):
    if bilangan_prima(i):
        continue
    elif i % 3 == 0 and i % 5 == 0:
        angka.append("FooBar")
    elif i % 3 == 0:
        angka.append("Foo")
    elif i % 5 == 0:
        angka.append("Bar")
    else:
        angka.append(i)

print(angka)