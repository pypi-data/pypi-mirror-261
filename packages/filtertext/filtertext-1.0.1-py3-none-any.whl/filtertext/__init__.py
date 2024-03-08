__all__ = [
    "TextFilter", 
    "RemoveDuplicatedLinesTextFilter", 
    "RemoveWhitespaceLinesTextFilter"
]

from pathlib import Path

class TextFilter:
    def __init__(self, data=None):
        self._text = ""
        if data:
            if isinstance(data, TextFilter):
                self._text = data.text
            elif Path(data).is_file():
                with open(data, "r") as file:
                    self._text = file.read()
            elif isinstance(data, str):
                self._text = data
        
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = value

    @text.deleter
    def text(self):
        del self._text
        self._text = ""

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            _text = file.read()
        text_filter = cls()
        text_filter.text = _text
        return text_filter
    
    @classmethod
    def from_text(cls, text):
        text_filter = cls()
        text_filter.text = text
        return text_filter
    
    @classmethod
    def from_text_filter(cls, text_filter):
        _text_filter = cls()
        _text_filter.text = text_filter.text
        return _text_filter
    
    def filter(self, data=None, **kwargs):
        if data:
            if isinstance(data, TextFilter):
                self._text = data.text
            elif Path(data).is_file():
                with open(data, "r") as file:
                    self._text = file.read()
            elif isinstance(data, str):
                self._text = data


class RemoveDuplicatedLinesTextFilter(TextFilter):
    def __init__(self, data=None):
        super().__init__(self, data)

    def filter(self, data=None, **kwargs):
        super().filter(data, kwargs=kwargs)
        line_set = set()
        self._text = '\n'.join(line_set.update(self._text.split('\n')))


class RemoveWhitespaceLinesTextFilter(TextFilter):
    def __init__(self, data=None):
        super().__init__(self, data)

    def filter(self, data=None, **kwargs):
        super().filter(data, kwargs=kwargs)

        filtered_lines = []
        lines = self._text.split('\n')
        for line in lines:
            if line.strip() != "":
                filtered_lines.append(line.strip())
        self._text = '\n'.join(filtered_lines)