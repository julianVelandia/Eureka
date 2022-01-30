from bs4 import BeautifulSoup
import requests
import


class Request:

    def single_request(self, model.Path):
        # TODO regular expresion
        return True

    url = requests.get(URL)

    soup = BeautifulSoup(url.content, "html.parser")
    result = soup.find("h1", {"class": "product-name__name alkosto-title-color"})
