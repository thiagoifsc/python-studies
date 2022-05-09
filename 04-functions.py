#define function
def hi(name):
    print("Hi", name)

#call the function
hi("Thiago")

#define function with return
def pair(number):
    if number % 2 == 0:
        out="Pair"
    else:
        out="Not pair"
    return out

#print function return
print(pair(7))
print(pair(16))