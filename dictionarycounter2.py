word = 'brontosaurus'
d = dict()
for alphabet in word:
    d[alphabet] = d.get(alphabet,0) + 1
print (d)