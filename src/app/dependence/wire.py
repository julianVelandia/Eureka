from src.handler.handler import Handler


class HandlerContainer:
    GetInformationHandler: Handler

def new_wire() -> HandlerContainer:
    conf = GetConfig()