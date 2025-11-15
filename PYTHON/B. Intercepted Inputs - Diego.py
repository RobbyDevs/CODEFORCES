def multiplos(n):
 
	a = 1
	b = n
 
	lista = [(a,b)]
 
	while a < b//a:
		a += 1
 
		if n % a == 0:
			d = n//a
			if (a * d) == n:
				lista.append((a,d))
 
	return lista
	
a = int(input())
 
 
for i in range(a):
	x = input()
	l = [int(i) for i in input().split()]
	
 
	
	m = multiplos(len(l)-2)
 
	for w in m:
		if w[0] in l and w[1] in l:
			print(w[0],w[1])
			break