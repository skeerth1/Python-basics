# functions - starts with def

def print_max(a,b):
    if a>b:
        print('a is maximun')
    elif a==b:
        print('a is equal to b')
    else:
        print('b is maximum')

# directly pass the literal values
print_max(3,4)
x = 5
y = 7
# pass variables as arguments
print_max(x,y)

def sayHello(name='Sam'):
    print(f'Hello {name}')

sayHello()
