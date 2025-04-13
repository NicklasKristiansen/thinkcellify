from functools import singledispatch




def row_settings_dispatch(func):
    allowed_settings = {"row", "row_index", "data_type", "color"}

    registry = {}
    registry[NotImplemented] = func


    def dispatch(settings_str):
        if settings_str not in allowed_settings:
            settings_str = NotImplemented
        return registry[settings_str]















