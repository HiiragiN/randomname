import random


def get_birth_with_starsign():
    year = random.randint(1972, 2002)
    month = random.randint(1, 12)
    m_to_days = {
        "1": (1, 31),
        "2": (1, 29),
        "3": (1, 31),
        "4": (1, 30),
        "5": (1, 31),
        "6": (1, 30),
        "7": (1, 31),
        "8": (1, 31),
        "9": (1, 30),
        "10": (1, 31),
        "11": (1, 30),
        "12": (1, 31),
    }
    day = random.randint(*m_to_days[str(month)])

    birthday = f'{year}.{month}.{day}'

    constellation = "False"

    if month == 1:
        if day > 20:
            constellation = "11"
        if day <= 20:
            constellation = "10"
    if month == 2:
        if day <= 18:
            constellation = "11"
        if day > 18:
            constellation = "12"
    if month == 3:
        if day > 20:
            constellation = "1"
        if day <= 20:
            constellation = "12"
    if month == 4:
        if day > 19:
            constellation = "2"
        if day <= 19:
            constellation = "1"
    if month == 5:
        if day > 20:
            constellation = "3"
        if day <= 20:
            constellation = "2"
    if month == 6:
        if day > 20:
            constellation = "4"
        if day <= 20:
            constellation = "3"
    if month == 7:
        if day > 20:
            constellation = "5"
        if day <= 20:
            constellation = "4"
    if month == 8:
        if day > 20:
            constellation = "6"
        if day <= 20:
            constellation = "5"
    if month == 9:
        if day > 20:
            constellation = "7"
        if day <= 20:
            constellation = "6"
    if month == 10:
        if day > 20:
            constellation = "8"
        if day <= 20:
            constellation = "7"
    if month == 11:
        if day > 20:
            constellation = "9"
        if day <= 20:
            constellation = "8"
    if month == 12:
        if day > 20:
            constellation = "1"
        if day <= 20:
            constellation = "9"


    return birthday, constellation


if __name__ == "__main__":
    # pass
    print(get_birth_with_starsign())