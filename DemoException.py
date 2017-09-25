class NetworkError(RuntimeError):
    """docstring for NetworkError"""

    def __init__(self, arg1, arg2):
        super(NetworkError, self).__init__()
        self.arg1 = arg1
        self.arg2 = arg2


def main():
    try:
        raise NetworkError("Bad Hostname", "Bad String")
    except NetworkError as e:
        print('Exception rised due to %s and %s' % (e.arg1, e.arg2))
    else:
        print('No Exception raised')
    finally:
        print('In finally')


if __name__ == '__main__':
    main()
