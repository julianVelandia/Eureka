from internal.information.core.entity.path import Path


class PathModel(Path):

    def __init__(self,
                 section_id,
                 base_url,
                 text_tag,
                 text_class_name,
                 children_tag,
                 ):
        Path.__init__(self,
                      section_id,
                      base_url,
                      text_tag,
                      text_class_name,
                      children_tag,
                      )

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
