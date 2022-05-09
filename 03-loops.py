#for
for letter in "Test":
    print(letter)

list = [1, 'Test', 'a']
for item in list:
    print(item)

print(list[1])


#while
i=1
while i <=5:
    print(i)
    i +=1


#iterators
my_test = range(1,3)
my_iterrator = my_test.__iter__()

for c in my_test:
    print(my_iterrator.__next__())

print([z for z in range(10) if z > 7])
