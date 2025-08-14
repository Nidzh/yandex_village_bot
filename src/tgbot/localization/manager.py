from src.tgbot.localization.data import available_languages, localization_data


class TextManager:
    def __init__(self, lang_code: str | None, data: dict = localization_data):
        if lang_code not in available_languages:
            lang_code = available_languages[0]

        self.lang_code = lang_code
        self.data = data

    def get_text(self, obj):
        if isinstance(obj, dict):
            if self.lang_code in obj:
                return obj[self.lang_code]
            else:
                return TextManager(lang_code=self.lang_code, data=obj)

    def __getattr__(self, item):
        if item in self.data:
            return self.get_text(self.data[item])
        raise AttributeError(f"No such attribute: {item}")
