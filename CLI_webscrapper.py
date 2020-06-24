from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import numpy as np


def getSoup(address):
    page = requests.get(address)
    soup = BeautifulSoup(page.content, "html.parser")

    time_tag = soup.find_all("time")
    h2_tag = soup.find_all("h2", class_="h3")
    article_tag = soup.find_all("a", class_="emphasis")
    article_dict = dict()
    for i in range(0, 6):
        if not bool(article_dict):
            article_dict = {
                "date_published": [time_tag[i].get_text().strip()],
                "article_title": [h2_tag[i].get_text().strip()],
                "Journal_Published_in": [article_tag[i].get_text().strip()],
            }
        else:
            article_dict["date_published"].append(time_tag[i].get_text().strip())
            article_dict["article_title"].append(h2_tag[i].get_text().strip())
            article_dict["Journal_Published_in"].append(
                article_tag[i].get_text().strip()
            )

    print(article_dict)
    article_df = pd.DataFrame.from_dict(article_dict, orient="columns")

    path = input("What is the file path you wish to use:")
    filename = input("What would you like to name the file:")
    text_write(path, filename, article_df)


def text_write(path, filename, df):
    filepath = os.path.join(path, filename)
    df.to_csv(filepath, sep="\t")

