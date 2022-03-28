#Conjuntos

a = {1, 2, 3}
b = {3, 4, 5}

#print(a == b)

c = {5, 6, 7}
d = { 7, 6, 5}

h = {1, 2, 3, 4, 5, 6} 
#print(c == d)

#Como unir dos conjuntos
e = a | b
#print(e)

#Intersección de dos conjuntos
f = a & b
#print(f)

#print(len(b))

#Diferencia de conjuntos (Elementos de A que no están en B)
g = a - b 
#print(g)

#Diferencia simétrica(Elememtos que estan en A y en B pero no están en ambos)
h = a ^ b
#print(h)

#Determinar si un conjunto es subconjunto de otro
#print(h.issubset(b))

#Determinar superconjuntos
#print(c.issuperset(h))
print(a.isdisjoint(b))