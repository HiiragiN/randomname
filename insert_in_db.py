from scraping_name import random_name
from conv_address import generate_email
from create_birth import get_birth_with_starsign
from database import connection
from job import joblist
import random
import time

def insert_base_data(db_connection, sex='male', sei_rarity="", mei_rarity=""):
    first_names, last_names = random_name(sex=sex, sei_rarity=sei_rarity, mei_rarity=mei_rarity)

    with db_connection.cursor() as cursor:
        sql_first = "insert into `myoji` (`kanji`, `kana`, `roma`) values (%s, %s, %s)"
        sql_last = "insert into `name` (`kanji`, `kana`, `roma`, `gender`) values (%s, %s, %s, %s)"

        cursor.executemany(sql_last, last_names)
        cursor.executemany(sql_first, first_names)
        connection.commit()

def insert_joblist(db_connection):
    job_list = joblist()

    with db_connection.cursor() as cursor:
        sql = "insert into `job` (`job`) values (%s)"

        cursor.executemany(sql, job_list)
        connection.commit()

def generate_user(db_connection):
    with db_connection.cursor() as cursor:
        sql = """
        select m.kanji as `myoji_kanji`, m.kana as 'myoji_kana', m.roma as `myoji_roma`, 
        n.kanji as `name_kanji`, n.kana as 'name_kana', n.roma as `name_roma`, n.gender as `gender` 
        j.job as `job` from `myoji` as m, name as n, `job` as j order by RAND() LIMIT 10
        """
        cursor.execute(sql)
        user_datas = cursor.fetchall()

    user_data = user_datas[0]
    age, birthday, constellation = get_birth_with_starsign()  # type: ignore
    income = generate_income()

    user_data["full_name"] = user_data["myoji_kanji"] + " " + user_data["name_kanji"]

    user_data["full_name_kana"] = user_data["myoji_kana"] + " " + user_data["name_kana"]

    user_data["gender"] = user_data["gender"]

    user_data["email"] = generate_email(first=user_data["name_roma"], last=user_data["myoji_roma"])

    user_data["birthday"] = birthday

    user_data["starsign"] = constellation

    user_data["income"] = income

    return user_data


def many_generate_user(db_connection):
    with db_connection.cursor() as cursor:
        sql = """
        select m.kanji as `myoji_kanji`, m.kana as 'myoji_kana', m.roma as `myoji_roma`, 
        n.kanji as `name_kanji`, n.kana as 'name_kana', n.roma as `name_roma`, n.gender as `gender`
        from `myoji` as m, `name` as n order by RAND() limit 1000
        """

        cursor.execute(sql)
        all_user_data = cursor.fetchall()

        new_user_data_list = []

        for user_data in all_user_data:
            # Get random birthday and constellation
            birthday, constellation = get_birth_with_starsign()

            real_user_data = {}

            # Assignment and list sorting
            real_user_data["fullname"] = user_data[0] + " " + user_data[3]
            real_user_data["read_fullname"] = user_data[1] + " " + user_data[4]
            real_user_data["email"] = generate_email(first=user_data[2], last=user_data[5])
            real_user_data["hobby"] = generate_hobby()
            real_user_data["birthday"] = birthday
            real_user_data["starsign"] = constellation
            real_user_data["gender"] = user_data[6]
            real_user_data["job"] = joblist()[0]
            real_user_data["income"] = generate_income()

            new_user_data_list.append(list(real_user_data.values()))
            # random.shuffle(new_user_data_list)
        return new_user_data_list


# def insert_desc_user_data(full_name, read_fullname, email, birthday, starsign, gender, income):
#
#     with connection.cursor() as cursor:
#
#         sql = "insert into `user_data` (full_name, read_fullname, email, birthday, starsign, gender, income" \
#               ") values (%s, %s, %s, %s, %s, %s, %s)"
#
#         cursor.executemany(sql, (full_name, read_fullname, email, age, birthday, starsign, gender, income))
#         connection.commit()

def insert_batch_user_data(data):
    with connection.cursor() as cursor:
        sql = """
        insert into `user_data` (fullname, read_fullname, email, hobby, birthday, starsign, gender, job, income) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        cursor.executemany(sql, data)
        connection.commit()

def generate_income():
    income = {
        "1": "200万円以下",
        "2": "200万円〜300万円",
        "3": "300万円〜400万円",
        "4": "400万円〜500万円",
        "5": "500万円〜600万円",
        "6": "600万円〜700万円",
        "7": "700万円〜800万円",
        "8": "800万円〜900万円",
        "9": "1000万円以上",
    }
    # code of one's own work
    # number, _income = random.choice(list(income.items()))

    return income[str(random.randint(1, len(income)))]


def generate_hobby():
    hobby = ["Reading", "Film Appreciation", "Learning English", "Tanking Picture", "jogging", "Listen to Music",
            "Meditation", "View Sports", "Game", "Cooking", "DIY", "Golf", "Tennis", "visiting multiple Onsen",
            "Bouldering", "Fishing", "Dirt", "Camp", "Gym", "Bike", "strain", "Program", "Art"]

    return random.choice(hobby)


if __name__ == "__main__":
    #jobのテーブルにデータを入れている
    # insert_joblist(db_connection=connection)

    # ループ処理で一つずつデータを入れている。
    # for i in range(0, 100):
    #     g = generate_user(db_connection=connection)
    #
    #     insert_desc_user_data(full_name=g["full_name"], read_fullname=g["full_name_kana"],
    #                           email=g['email'], birthday=g["birthday"], starsign=g["starsign"],
    #                           gender=g["gender"], income=g["income"])


    # データを作って一気にsqlに入れている
    # user_data_result = many_generate_user(db_connection=connection)
    # insert_batch_user_data(data=user_data_result)

    # 名前データを入れるもの
    insert_base_data(db_connection=connection, sex="male", sei_rarity="20", mei_rarity="18")
    # sei_rarity=9~20, mei_rarity=10~19