from internal.information.core.entity.information import Information


class InformationModel(Information):

    def __init__(self, uuid, link, text):
        Information.__init__(self, uuid, link, text)
