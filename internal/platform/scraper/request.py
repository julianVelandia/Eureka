from bs4 import BeautifulSoup
import requests

from internal.platform.scraper.models.path import Path

from internal.platform.scraper.models.response import Response

CLASS = "class"
PARSER = "html.parser"


def single_request(path: Path):
    response = Response()

    url = requests.get(Path.base_url)
    soup = BeautifulSoup(url.content, PARSER)

    class_names_title = format_class_names(path.title_class_name)
    response.title = soup.find(path.title_tag, {CLASS: class_names_title}).text

    # TODO para el texto o contenido
    # TODO hacer esa parte modular
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
