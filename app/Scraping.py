import requests
from bs4 import BeautifulSoup
from .conexcionBD import SessionLocal
from .CRUD import create_cita

def scrape():
    db = SessionLocal()
    url = "https://quotes.toscrape.com"
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for quote_div in soup.select(".quote"):
            texto = quote_div.select_one(".text").get_text(strip=True)
            autor = quote_div.select_one(".author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote_div.select(".tag")]

            create_cita(db, texto, autor, tags)

        next_btn = soup.select_one("li.next > a")
        url = f"https://quotes.toscrape.com{next_btn['href']}" if next_btn else None
