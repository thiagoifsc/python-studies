#string
if 5 > 2:
     print("Five is greater than two")

teste = "Hello World"
print(teste)
print(type(teste))

#int
a = 5
print(a)
print(type(a))

#float
b = 120.5
print(b)
print(type(b))

#complex
c = -1j
print(c)
print(type(c))

#math
print(b-a)

#list
d = ["Laranja", "Maçã", "Pera"]
print(d)
print(type(d))
print(d[0])

#tuple
e = ("Laranja", "Maçã", "Pera")
print(e)
print(type(e))

#range
f = range(10)
print(f)
print(type(f))

#dict
g = {"name" : "Thiago", "age" : 33}
print(g)
print(type(g))
print (g['name'])
print("name" in g)
print(len(g))
print(g.get("age"))
print(g.items())
print(g.keys())

#set
f = {"Laranja", "Maçã", "Pera"}
print(f)
print(type(f))

#fronzenset
g = ({"Laranja", "Maçã", "Pera"})
print(g)
print(type(g))

#bool
h = True
print(h)
print(type(h))

#bytes
i = b"Hello"
print(i)
print(type(i))

#bytearray
j = bytearray(2)
print(j)
print(type(j))

#memoryview
k = memoryview(bytes(10))
print(k)
print(type(k))