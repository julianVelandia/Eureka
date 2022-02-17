class PathModel:
    section_id: str
    base_url: str
    text_tag: str
    text_class_name: [str]
    children_tag: str

    def __init__(self,
                 section_id: str,
                 base_url: str,
                 text_tag: str,
                 text_class_name: [str],
                 children_tag: str):
        self.section_id = section_id
        self.base_url = base_url
        self.text_tag = text_tag
        self.text_class_name = text_class_name
        self.children_tag = children_tag
