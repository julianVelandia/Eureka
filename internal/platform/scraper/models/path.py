class Path:
    def __init__(self, base_url, title, text, sub_path):
        self.base_url = base_url
        self.title = title
        self.text = text
        self.sub_path = sub_path

    base_url: str
    title: str
    text: [str]
    sub_path: [str]


class SubPath:
    url: str
    title: str
    text: [str]

