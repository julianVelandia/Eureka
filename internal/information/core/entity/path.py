from dataclasses import dataclass


@dataclass(frozen=True)
class Path:
    section_id: str
    base_url: str
    text_tag: str
    text_class_name: [str]
    children_tag: str
