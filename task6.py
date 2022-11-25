import random as rd


def hash(input):
    ''''Hash function that converts the input to string to
    be able to use the ASCII values'''
    inputstr = str(input)
    total = 0

    for i, char in enumerate(inputstr):
        total += ord(char) * 31**i

    total *= 247
    total = total // 61
    total = total % 256

    return total


def write_file(file_name, content):
    with open(file_name, "w", encoding="utf-8") as file:
        for char in content:
            file.write(str(char))
            file.write("\n")


def hash_test(table, input_amount):
    '''Chi-squared test'''
    buckets = 255
    sum = 0

    for key, value in table.items():
        sum += (value * (value + 1)) / 2

    sum = sum / ((input_amount/(2*buckets))*(input_amount + 2*buckets - 1))
    print(f"Uniformity = {round(sum, 2)}")


def str_to_binary(string):
    binary = format(ord(string), '08b')
    print(f"Binary for {string} = {binary}")


def main():
    inputValue = '539601837'
    random_input = [rd.randint(0, 5000000) for i in range(3000)]
    hash_value = hash(inputValue)
    hash_avalanche = dict()
    hash_uniformity = dict()
    values = []
    keys = []
    print(f"hash value: {hash_value}")

    for i in range(1000):
        hash_value = hash(inputValue)
        if hash_avalanche.get(hash_value) is not None:
            value = hash_avalanche.get(hash_value) + 1
            hash_avalanche.update({hash_value: value})
        else:
            hash_avalanche.update({hash_value: 1})
        if type(inputValue) == str:
            inputValue = str(ord(inputValue) + 1)
        else:
            inputValue += 1

    for key, item in hash_avalanche.items():
        values.append(item)
        keys.append(key)
        print(f"Key: {key}, Value: {item}")

    for input in random_input:
        hash_value = hash(input)
        if hash_uniformity.get(hash_value) is not None:
            value = hash_uniformity.get(hash_value) + 1
            hash_uniformity.update({hash_value: value})
        else:
            hash_uniformity.update({hash_value: 1})

    hash_test(hash_uniformity, 3000)
    values.sort()
    keys.sort()
    write_file("values.txt", values)
    write_file("keys.txt", keys)


if __name__ == "__main__":
    main()
