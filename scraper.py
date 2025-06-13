import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_articles():
    url = "https://techcrunch.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.select("a.post-block__title__link")[:20]:
        title = item.get_text(strip=True)
        link = item.get('href')
        articles.append({
            "title": title,
            "link": link,
            "timestamp": datetime.utcnow().isoformat()
        })

    return articles
