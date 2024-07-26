from bs4 import BeautifulSoup
import requests
import regex as re

from kana_to_roma import kana_to_roma


def random_name(sex="male", sei_rarity="", mei_rarity=""):
    url = f"https://namegen.jp/?country=japan&sex={sex}&middlename=&middlename_cond=fukumu&middlename_rarity=&middlename_rarity_cond=ika&lastname=&lastname_cond=fukumu&lastname_rarity={sei_rarity}&lastname_rarity_cond=ika&lastname_type=name&firstname=&firstname_cond=fukumu&firstname_rarity={mei_rarity}&firstname_rarity_cond=ika&firstname_type=name"
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "html.parser")
    body = soup.find('form', method='GET')
    readnames = []
    first_name = []
    last_name = []

    if sex == "male":
        tr = body.find_all('tr') # type: ignore
        full_names = [td.find_all('a') for td in soup.select('td.name')]
        readnames = [_readname.find('td', class_='pron').text.split(" ")
                    for _readname in tr if _readname.find('td', class_='pron')]


        for full_name in full_names:
            last_name.append([full_name[0].text])
            first_name.append([full_name[1].text])

    if sex == "female":
        tr = body.find_all('tr') # type: ignore
        full_names = []
        _full_names = [td.find_all(string=True) for td in soup.select('td.name')]
        for _full_name in _full_names:
            full_name = list(filter(("\n").__ne__, _full_name))
            full_name = [re.sub(r'[\n\s]', '', f) for f in full_name]
            full_names.append(full_name)

        readnames = [_readname.find('td', class_='pron').text.split(" ")
                    for _readname in tr if _readname.find('td', class_='pron')]

        for full_name in full_names:
            last_name.append([full_name[0]])
            first_name.append([full_name[1]])

    for i, readname in enumerate(readnames):
        last_name[i].append(readname[0])
        last_name[i].append(kana_to_roma(readname[0]))

        first_name[i].append(readname[1])
        first_name[i].append(kana_to_roma(readname[1]))
        first_name[i].append(sex)

    return last_name, first_name


if __name__ == "__main__":
    # sei_rarity=9~20, mei_rarity=10~19
    print(random_name(sex="male", sei_rarity="20", mei_rarity="19"))