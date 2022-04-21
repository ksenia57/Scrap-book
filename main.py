import requests
from bs4 import BeautifulSoup as bs

def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    }

   # req = requests.get(url, headers) # get запрос

   # with open("project.html", "w", encoding="utf-8") as file:
   #      file.write(req.text)

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

    # with open(f"data/{project_name}.html", "w", encoding="utf-8") as file:
    #     file.write(req.text)

    with open(f"data/{project_name}.html", encoding="utf-8") as file:
        src = file.read()

    soup = bs(src, "lxml")
    project_data = soup.find("div", class_="product-detail-page__body")

# обложка книги
    try:
        project_obl = "https:" + project_data.find("picture", class_="product-poster__main-picture").find("img").get("src")
        print(project_obl)
    except Exception:
        project_obl = "NaN"

# название
    try:
        if project_data.find("div", class_="product-characteristic__label-holder").find("span").text == " Автор: ":
            project_name = project_data.find("div", class_="product-detail-page__title-holder").find("h1").text
            project_name = project_name.split(':')[-1][1:]
            print(project_name)
    except Exception:
        project_name = "NaN"

# автор
    try:
        project_author = project_data.find("div", class_="product-characteristic__value").find("a").text
        print(project_author)
    except Exception:
        project_author = "NaN"

# описание
    try:
        project_disc = project_data.find("div", class_="product-about__text").text
        print(project_disc)
    except Exception:
        project_disc = "NaN"

#
    project_charac = soup.find("div", class_="product-characteristic product-detail-page__product-characteristic")
    harac = project_charac.find_all(class_="product-characteristic__item-holder")

    for har in harac:
        if har.find("span", class_="product-characteristic__label").text == " Раздел: ":
            project_section = har.find("a", class_="product-characteristic-link smartLink").text
            print(project_section)
        if har.find("span", class_="product-characteristic__label").text == " Издательство: ":
            project_publish = har.find("a", class_="product-characteristic-link smartLink").text
            print(project_publish)
        # if har.find("span", class_="product-characteristic__label").text == " Возрастное ограничение: ":
        #     project_age = har.find("a", class_="product-characteristic-link smartLink").
        #     print(project_age)
        # if har.find("span", class_="product-characteristic__label").text == " Год издания: ":
        #     project_year = har.find("a", class_="product-characteristic-link smartLink").
        #     print(project_year)
        # if har.find("span", class_="product-characteristic__label").text == " Количество страниц: ":
        #     project_pages = har.find("a", class_="product-characteristic-link smartLink").
        #     print(project_pages)

    # for project_har in project_harac[0:1]:
    #     project_disc = project_data.find("div", class_="product-about__text").text
    #     print(project_disc)

get_data("https://book24.ru/catalog/fiction-1592/")