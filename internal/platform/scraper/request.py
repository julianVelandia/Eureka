from bs4 import BeautifulSoup
import requests

from internal.platform.scraper.models.path import Path

from internal.platform.scraper.models.response import Response

CLASS = "class"
PARSER = "html.parser"


def single_request(path: Path):
    response = Response("")

    url = requests.get(path.base_url)
    soup = BeautifulSoup(url.content, PARSER)

    class_names_text = format_class_names(path.text_class_name)
    response.text = soup.find(path.text_tag, {CLASS: class_names_text}).text

    return response


def format_class_names(names: [str]):
    class_names = ""
    first = True
    for name in names:
        if not first:
            class_names += " "
        first = False
        class_names += name

    return class_names
