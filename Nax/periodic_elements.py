from periodictable import elements
symbols = ['Ag', 'Hg', 'Ta', 'Sb', 'Po', 'Pd', 'Hg', 'Pt', 'Lr']
numbers={x.symbol:x.number for x in elements}
ans = []
for el in symbols:
	ans.append(chr(numbers[el]))
print(''.join(ans))