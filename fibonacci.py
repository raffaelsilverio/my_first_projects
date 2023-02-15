# my first project
def fib(number):
    a = 0
    b = 1
    print(a, end= ' ')
    print(b, end= ' ')
    for i in range(number-2):
        c = a + b
        print(c, end=' ')
        a = b
        b = c


def main():
    n = int(input('How many number do you want?'  ))
    fib(n)


if __name__ == '__main__':
    main()