from bs4 import BeautifulSoup
import requests
import re

from internal.information.infrastructure.getpath.config.model.path import PathModel
from internal.information.infrastructure.request.model.information import InformationModel
from internal.information.infrastructure.request.process import ProcessInformation


CLASS = "class"
PARSER = "html.parser"


class Request(ProcessInformation):
    def single_request(self, path: PathModel) -> InformationModel:
        response = InformationModel()

        # TODO try and catch

        url = requests.get(path.base_url)
        soup = BeautifulSoup(url.content, PARSER)

        class_names_text = self.format_class_names(path.text_class_name)
        response.text = soup.find(path.text_tag, {CLASS: class_names_text}).text

        return response

    def format_class_names(self, names: [str]):
        class_names = ""
        first = True
        for name in names:
            if not first:
                class_names += " "
            first = False
            class_names += name

        return class_names

    def url_is_valid(self, path: str) -> bool:
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, path) is not None
