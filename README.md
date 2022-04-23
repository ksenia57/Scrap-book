## Web-scraping of a site with books
Take Book24 as an example.
### To do:
#### (implemented in [main](https://github.com/ksenia57/Scrap-book/blob/master/main.py))
+ We open the section of interest to us. In my case, this is Fiction books, popular queries.
+ We pull out links to the personal page of each book.
+ For convenience, the code of each page will be stored in the data folder in the file with the title of the book.
+ We pull out the title, author, description, section, publisher, age limit, year of publication, number of pages, rating. If any string is missing, it is assigned the value NaN.
+ We add try-except constructs to avoid errors in the program. If any book parameter is missing, then it is NaN.
+ We create the list project_data_list.
+ We write the dictionary to json file.
+ Add a for loop to iterate through all the pages in the Fiction books.
### Result:
Get [json file](https://github.com/ksenia57/Scrap-book/blob/master/project_book.json) with data.