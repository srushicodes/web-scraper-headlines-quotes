
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Quotes
    quotes = soup.find_all("span", class_="text")

    with open("quotes.txt", "w", encoding="utf-8") as file:
        for quote in quotes:
            file.write(quote.text.strip() + "\n")

    print("Quotes scraped successfully!")
    print("Saved in quotes.txt")

    # Headlines
    headlines = soup.find_all("h2")

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for headline in headlines:
            file.write(headline.text.strip() + "\n")

    print("Headlines scraped successfully!")
    print("Saved in headlines.txt")

else:
    print("Failed to access the website.")