from internal.information.core.entity.information import Information


class InformationModel(Information):
    uuid: str
    link: str
    text: str

    def __init__(self, uuid, text, link):
        Information.__init__(self, uuid, text, link)
