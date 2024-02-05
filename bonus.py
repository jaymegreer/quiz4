print("Input string or int values into the array of length 3 -")

inputArray = []

for i in range(3):
    value = input("Value: ")
    inputArray.append(value)

for element in inputArray:
    count = 0
    for char in element:
        count += 1
    print(count)


