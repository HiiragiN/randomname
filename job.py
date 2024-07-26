from bs4 import BeautifulSoup
import requests
import random

url = "https://aaaaaa.co.jp/job/joblist/"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "html.parser")

job_titles = soup.select("#sitemap_list > li > ul > li > a")

result = []

def joblist():
    for job_title in job_titles:
        result.append(job_title.text.split("（")[0])
    # return result

    job = random.choice(result)
    return job,

if __name__ == "__main__":
    print(joblist()[0])
    print(type(joblist()))