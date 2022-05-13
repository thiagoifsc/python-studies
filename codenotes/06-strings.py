from datetime import datetime

#methods
text = "Hello World"

print(text.replace("World", "User").upper())

my_age = 33

print(f'My age is {my_age}')
print('My age is', my_age)

print(f'{my_age=}')

today=datetime.today()
time=datetime.now()
print(f"{today:%B %d, %Y}")
print(f"Now: {time:%H:%M:%S}")
