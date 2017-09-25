import sys


def Cat(filename):
    f = open(filename, 'rU')
    # for line in f:
    # print(line,end="");

    # lines = f.readlines();

    lines = f.read()
    print(lines)
    f.close()


def Hello(name):
    if(name == 'Pawan' or name == 'Lucky'):
        print('Pawan in if')
    name = name + '!!!!!'
    print('Hello', name, 'hi')


def main():
    # Cat(sys.argv[1])
    i = 0
    while True:
        print(i)
        i += 1
        if (i == 5):
            break
    try:
        f = open('nofile','rU')
    except Exception as e:
        print('in except')
        # raise e
    finally:
        print('in finally')


# boilerplate to invoke main()
if __name__ == '__main__':
    main()
