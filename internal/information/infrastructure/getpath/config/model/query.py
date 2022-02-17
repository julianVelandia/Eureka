class QueryModel:
    language: str
    file_name: str

    def __init__(self, language: str, file_name: str):
        self.language = language
        self.file_name = file_name
