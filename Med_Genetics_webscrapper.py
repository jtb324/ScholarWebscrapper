##################################################################################
# This file searches the journal of Medical Genetics for the the date published, the article title,
# and the journal it was published in

##################################################################################
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd


##################################################################################
def text_write(path, filename, df):
    """This function just writes the provided dataframe to a file"""
    filepath = os.path.join(path, filename)
    df.to_csv(filepath, sep="\t")


def getSoupMedGenetics(address):
    page = requests.get(address)
    soup = BeautifulSoup(page.content, "html.parser")

    time_tag = soup.find_all("span", class_="highwire-cite-metadata-date")
    title_tag = soup.find_all("span", class_="highwire-cite-title")
    author_tag = soup.find_all("span", class_="highwire-citation-author")
    article_tag = soup.find_all("span", class_="highwire-cite-metadata-journal")

    article_dict = dict()

    for i in range(0, 6):
        if not bool(article_dict):
            article_dict = {
                "date_published": [time_tag[i].get_text().strip()],
                "article_title": [title_tag[i].get_text().strip()],
                "authors": [author_tag[i].get_text().strip()],
                "Journal_Published_in": [article_tag[i].get_text().strip()],
            }
        else:
            article_dict["date_published"].append(time_tag[i].get_text().strip())
            article_dict["article_title"].append(title_tag[i].get_text().strip())
            article_dict["authors"].append(author_tag[i].get_text().strip())
            article_dict["Journal_Published_in"].append(
                article_tag[i].get_text().strip()
            )

    article_df = pd.DataFrame.from_dict(article_dict, orient="columns")

    path = input("What is the file path you wish to use:")
    filename = input("What would you like to name the file:")
    text_write(path, filename, article_df)

