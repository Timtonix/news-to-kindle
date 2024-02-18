import requests
from bs4 import BeautifulSoup
import bdd


class InterScraper:
    def __init__(self):
        self.base_url = "https://www.courrierinternational.com/magazine"
        self.r = requests.get(self.base_url)
        self.soup = BeautifulSoup(self.r.text, "html.parser")
        self.bdd = bdd.International()



    def reload_soup(self):
        self.r = requests.get(self.base_url)
        self.soup = BeautifulSoup(self.r.text, "html.parser")

    def get_last_article(self):
        articles = self.soup.findAll("article")
        return articles[0]

    def get_all_articles(self):
        return self.soup.findAll("article")

    def init_bdd(self):
        if not self.bdd.get_journeaux():

            articles = self.soup.findAll("article")

            for article in articles:
                lien = article.a.get["href"]
                numero = int(lien.split("-")[0].split("/")[-1])
                titre = article.h2.text.split(".")[-1].strip()
                date = article.find(class_="article").text

                self.bdd.cursor.execute("INSERT INTO journeaux VALUES (?,?,?,?)", (numero, titre, lien, date))
            self.bdd.con.commit()
