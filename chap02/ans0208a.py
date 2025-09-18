def square(x):
    return x*x

def cube(x):
    return x**3

if __name__ == '__main__':
    print(square(5))
    x = 11
    print(f'square of {x} = {square(x)}')

    x = 3
    print(f'cube of {x} = {cube(x)}')

