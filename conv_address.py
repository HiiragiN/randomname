import random
import pymysql


domain = [
    "@yahoo.co.jp",
    "@gmail.com",
    "@ezweb.ne.jp",
    "@au.com ",
    "@docomo.ne.jp",
    "@i.softbank.jp",
    "@softbank.ne.jp",
    "@excite.co.jp",
    "@googlemail.com",
    "@hotmail.co.jp",
    "@hotmail.com",
    "@icloud.com",
    "@live.jp",
    "@me.com",
    "@mineo.jp",
    "@nifty.com",
    "@outlook.com",
    "@outlook.jp",
    "@yahoo.ne.jp",
    "@ybb.ne.jp",
    "@ymobile.ne.jp"
]

def generate_email(name=None, first="", last=""):
    if name:
        address = name + random.choice(domain)
    else:
        address = first + "." + last + random.choice(domain)
    return address

if __name__ == "__main__":
    pass
    print(generate_email(name="takahashi.tomoyuki"))
    print(generate_email(first="takahashi", last="tomoyuki"))
