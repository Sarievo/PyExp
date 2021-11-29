# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from itertools import permutations


def probability():
    # Use a breakpoint in the code line below to debug your script.
    my_list = []
    for c in permutations("ABCDEF", 6):
        my_list.append(c)

    times = 0
    for i in my_list:
        for k in i:
            if k == 'A':
                break
            if k == 'B':
                times += 1
                break
    print(str(times) + " / " + str(len(my_list)))

    times = 0
    for i in my_list:
        a_or_c = False
        b = False

        for k in i:
            if not a_or_c and (k == 'A' or k == 'C'):
                a_or_c = True
                continue
            if a_or_c and k == 'B':
                b = True
                continue
            if b and (k == 'A' or k == 'C'):
                times += 1
                break
    print(str(times) + " / " + str(len(my_list)))

    times = 0
    for i in my_list:
        c1 = False
        for k in i:
            if k == 'A' or k == 'B':
                if c1:
                    times += 1
                    break

                c1 = True
            else:
                c1 = False
    print(str(times) + " / " + str(len(my_list)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    probability()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
