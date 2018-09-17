

def solutions():
    # a, b = map(int, input().strip().split(' '))
    a = 5
    b = 3

    for i in range(b):
        rectangle = ""
        for j in range(a):
            rectangle += "*"

        print(rectangle)

    # print(a + b)

    return 1


assert solutions() == 1