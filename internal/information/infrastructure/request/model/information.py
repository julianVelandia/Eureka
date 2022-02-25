class InformationModel:
    uuid: str
    link: str
    text: str

    def __init__(self, uuid: str, link: str, text: str):
        self.uuid = uuid
        self.link = link
        self.text = text
