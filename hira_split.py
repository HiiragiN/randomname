from scraping_name import random_name
import pymysql

x = random_name()

last_name = x[2]

first_name = x[3]

_many_name = []

def generate_hira_name():
    for i, n in enumerate(last_name):
        for j, m in enumerate(first_name):
            many_name = n + " " + m
            _many_name.append(many_name)

    split_names = [_split_name.split(" ") for _split_name in _many_name]

    # print(split_names)

    # hira_last_names = []
    # hira_first_names = []
    #
    # for _split_name in split_names:
    #     hira_last_names.append(_split_name[0])
    #     hira_first_names.append(_split_name[1])

    # print(last_names)
    # print(first_names)

    return split_names

if __name__ == "__main__":
    print(generate_hira_name())