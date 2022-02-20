class PathModel:
    section_id: str
    base_url: str
    text_tag: str
    text_class_name: [str]
    children_tag: str

    def __init__(self,
                 section_id,
                 base_url,
                 text_tag,
                 text_class_name,
                 children_tag,
                 ):
        self.section_id = section_id
        self.base_url = base_url
        self.text_tag = text_tag
        self.text_class_name = text_class_name
        self.children_tag = children_tag

    @classmethod
    def new_full_path(cls,
                      section_id,
                      base_url,
                      text_tag,
                      text_class_name,
                      children_tag,
                      ):
        cls.section_id = section_id
        cls.base_url = base_url
        cls.text_tag = text_tag
        cls.text_class_name = text_class_name
        cls.children_tag = children_tag
        return cls
