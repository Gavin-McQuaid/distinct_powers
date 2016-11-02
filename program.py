terms = []
a = 2

while a <= 100:
	b = 2
	while b<=100:
		if a ** b not in terms:
			terms.append(a**b)
		b += 1
	a += 1

print len(terms)
