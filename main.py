import requests
from bs4 import BeautifulSoup as bs

def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    }

  #  req = requests.get(url, headers) # get запрос

  #  with open("project.html", "w", encoding="utf-8") as file:
  #       file.write(req.text)

    with open("project.html", encoding="utf-8") as file:
         src = file.read()

    soup = bs(src, "lxml")
    articles = soup.find_all(class_="product-list__item")
    print(articles)

    project_urls = []
    for article in articles:
        project_url = "https://book24.ru" + article.find("div", class_="product-card__image-holder").find("a").get("href")
        project_urls.append(project_url)

    for project_url in project_urls[0:1]:
        req = requests.get(project_url, headers)
        project_name = project_url.split('/')[-2]

    with open(f"data/{project_name}.html", "w", encoding="utf-8") as file:
        file.write(req.text)

    with open(f"data/{project_name}.html", encoding="utf-8") as file:
        src = file.read()

    soup = bs(src, "lxml")
    project_data = soup.find("div", class_="product-detail-page__body")

    project_obl = project_data.find("picture", class_="product-poster__main-picture")

get_data("https://book24.ru/catalog/fiction-1592/")