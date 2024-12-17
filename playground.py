def test(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(test(1,2,3,4,5,6,7,8,9))
