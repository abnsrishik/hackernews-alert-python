from bs4 import BeautifulSoup
import requests
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASS")
to_email = os.environ.get("TO_EMAIL")

response = requests.get(url = "https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name = "span", class_ = "titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.text
    article_texts.append(text)

    link = article_tag.find(name = "a").get("href")
    article_links.append(link)

article_upvotes  = [int(score.text.split(" ")[0]) for score in soup.find_all(name = "span", class_ = "score")]
highest_upvotes_index = article_upvotes.index((max(article_upvotes)))

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = my_email, password = password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs= to_email,
        msg=f"Subject:{article_texts[highest_upvotes_index]}\n\n"
            f"Current Most Upvoted News is {article_links[highest_upvotes_index]}\n"
            f"Upvotes: {max(article_upvotes)}\n"
            f"Source: Hacker News"
    )
