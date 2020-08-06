word = 'brontosaurus'
d = dict()
for alphabet in word:
    if alphabet not in d:
        d[alphabet] = 1
    else:
        d[alphabet] = d[alphabet] +1

print (d)