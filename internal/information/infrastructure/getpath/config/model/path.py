class PathModel:
    section_id: str
    base_url: str
    text_tag: str
    text_class_name: [str]
    children_tag: str
    children_class_name: [str]

    def __init__(self,
                 section_id: str,
                 base_url: str,
                 text_tag: str,
                 text_class_name: [str],
                 children_tag: str,
                 children_class_name: [str]):
        self.section_id = section_id
        self.base_url = base_url
        self.text_tag = text_tag
        self.text_class_name = text_class_name
        self.children_tag = children_tag
        self.children_class_name = children_class_name

