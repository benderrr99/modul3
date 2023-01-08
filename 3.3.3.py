a=[56,9,11,2]
def list (a):
    b = ''.join(map(str, a))
    c = b.replace('', ',')
    d = c.split(',')
    d.sort(reverse=True)
    e = int(''.join(map(str, d)))
    return e
print(list(a))
a=list([3,81,5])
print(a)
