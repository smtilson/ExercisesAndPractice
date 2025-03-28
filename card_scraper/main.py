import requests
from bs4 import BeautifulSoup
import csv


def fetch_hwa_card_urls():
    # Send HTTP request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    url = "https://decksmith.app/hubworldaidalon/cards"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the page: {response.status_code}")
        return []
    # Parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    card_link_elements = soup.select("a.group")
    return [target["href"] for target in card_link_elements]


def fetch_card_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the page:{url}\nCode:{response.status_code}")
        return None
    soup = BeautifulSoup(response.content, "html.parser")
    imgs = soup.select("img")
    imgs = [img for img in imgs if img.get("alt")]
    if len(imgs) != 1:
        print("Something is wrong with the imgs that were found")
        return imgs
    img_src = imgs[0]["src"]
    name = imgs[0]["alt"]
    return {"name": name, "frontImageUrl": img_src}
    subtitle_divs = soup.select("div.italic")
    if len(subtitle_divs) != 1:
        print("Something is wrong with the subtitles that were found")
        return subtitle_divs
    subtitle_div = subtitle_divs[0]
    # this will not be used
    subtitle = subtitle_div.text.strip()
    name_div = subtitle_div.previous.previous
    name = name_div.text.strip()
    # more card data can be gleaned but it is dependent on the card type
    # and I don't want to figure that out yet.


def create_hwa_csv(filename, cards_data):
    fieldnames = [
        "id",
        "name",
        "quantity",
        "landscape",
        "set",
        "setType",
        "frontImageUrl",
        "backImageUrl",
        "gameImageUrl",
    ]
    base_id = "A12DFAFA-84B5-4965-A8A7-35E2A30000"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        first_line = {
            "id": "Hubworld: Aidalon",
            "name": "Hubworld: Aidalon",
            "gameImageUrl": "https://cf.geekdo-images.com/GSF1XABi4QyCvTXPZDgzjw__imagepage/img/x5b3FWRWXPLifWXoHcDaVkp73JI=/fit-in/900x600/filters:no_upscale():strip_icc()/pic8454145.jpg",
        }
        writer.writerow(first_line)
        for index, card in enumerate(cards_data):
            if card is not None:
                # add the id and quantity fields
                index = str(index + 1)
                id_number = index if len(index) == 2 else "0" + index
                card["id"] = base_id + id_number
                card["quantity"] = 2
                # add the landscape field
                card["landscape"] = "no"
                # add the set and setType fields
                card["set"] = "demo deck"
                card["setType"] = "demo deck"
                # add the backImageUrl and gameImageUrl fields
                card["backImageUrl"] = None
                card["gameImageUrl"] = None
                writer.writerow(card)
    print(f"CSV file '{filename}' created successfully with {len(cards_data)} cards.")


if __name__ == "__main__":
    urls = fetch_hwa_card_urls()
    data = [fetch_card_data(url) for url in urls]
    create_hwa_csv("hubworld_aidalon.csv", data)
