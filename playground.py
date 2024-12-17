def test(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(test(1,2,3,4,5,6,7,8,9))


class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="BMW",model="XM")
print(my_car.make)
print(my_car.model)
