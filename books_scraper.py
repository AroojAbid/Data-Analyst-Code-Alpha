import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

book_data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()

    book_data.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

df = pd.DataFrame(book_data)

df.to_csv("books.csv", index=False)

print(df.head())
print("Data saved successfully!")