def probability(max_layer):
    base = 1
    print(str(base))

    base_list = [1]

    layer = 1

    while layer < max_layer:
        layer += 1
        new_list = []

        base *= 2
        for i in base_list:
            new_list.append(i / 2)
            new_list.append(i / 2)

        new_list2 = [new_list[0]]

        i = 1
        n = len(new_list) - 1
        while i < n:
            new_list2.append(new_list.pop(i) + new_list.pop(i))
            n -= 2

        new_list2.append(new_list[len(new_list) - 1])

        base_list = new_list2
        print(str(layer) + ":" + str(base) + " " + str(base_list))

    num = 39
    result = 0
    while num < 60:
        result += base_list[num]
        num += 1
    print(result)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    probability(100)
