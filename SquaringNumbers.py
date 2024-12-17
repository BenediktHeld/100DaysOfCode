def squaredList(List):
    for i in range(len(List)):
        numbers[i] = numbers[i] * numbers[i]
    return List

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(numbers)
squared_numbers = squaredList(numbers)
print(squared_numbers)
