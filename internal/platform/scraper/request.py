from bs4 import BeautifulSoup
import requests

from internal.platform.scraper.models.path import Path
from internal.platform.scraper.models.response import Response

CLASS = "class"
PARSER = "html.parser"


class Request:
    def single_request(self, path: Path):
        response = Response()

        url = requests.get(Path.base_url)
        soup = BeautifulSoup(url.content, PARSER)

        class_names_title = format_class_names(path.title_class_name)
        response.title = soup.find(path.title_tag, {CLASS: class_names_title}).text

        #TODO para el texto o contenido
        #TODO hacer esa parte modular
        return response



def format_class_names(names: [str]):
    class_names = ""
    for name in names:
        class_names += name
        class_names += " "

    return class_names
