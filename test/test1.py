def test(a, b):
    try:
        print('%s今年%d岁了' % (a, int(b)))
    except Exception as msg:
        print('age input error + %s' % msg)


if __name__ == '__main__':
    a = input('你叫什么名字？：')
    b = input('今年你几岁了？：')
    test(a, b)