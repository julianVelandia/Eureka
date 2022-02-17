class PathModel:

    base_url: str
    text_tag: str
    text_class_name: [str]

    def __init__(self, base_url: str, text_tag: str, text_class_name: [str]):
        self.base_url = base_url
        self.text_tag = text_tag
        self.text_class_name = text_class_name
