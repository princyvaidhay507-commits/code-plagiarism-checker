import requests
from bs4 import BeautifulSoup


def search_online_code(keyword):

    url = f"https://github.com/search?q={keyword}&type=code"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    results = []

    for link in links[:10]:

        text = link.get_text(strip=True)

        if text:
            results.append(text)

    return results