
import requests
from html.parser import HTMLParser


API_URL = "https://en.wikipedia.org/w/api.php"


class HTMLCleaner(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text = []

    def handle_data(self, data):
        self.text.append(data)





def clean_html(raw_html):
    parser = HTMLCleaner()
    parser.feed(raw_html)
    return " ".join("".join(parser.text).split())





def search_research(topic, limit=3):

    params = {
        "action": "query",
        "list": "search",
        "srsearch": topic,
        "srlimit": limit,
        "format": "json"
    }

    headers = {
        "User-Agent": "AIResearchAgent/1.0 (student project)"
    }

    try:
        response = requests.get(
            API_URL,
            params=params,
            headers=headers,
            timeout=15
        )




        response.raise_for_status()
        data = response.json()

        results = data["query"]["search"]

        articles = []

        for result in results:
            articles.append({
                "title": result["title"],
                "snippet": clean_html(result["snippet"]),
                "url": (
                    "https://en.wikipedia.org/wiki/"
                    + requests.utils.quote(result["title"].replace(" ", "_"))
                )
            })


        return articles


    except requests.RequestException as error:
        print(f"Research error: {error}")
        return []




    except (KeyError, ValueError) as error:
        print(f"Could not process results: {error}")
        return []
