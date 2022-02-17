class InformationModel:
    uuid: str
    text: str
    link: str

    def __init__(self, uuid: str, text: str, link: str):
        self.text = text
        self.link = link
        self.uuid = uuid
