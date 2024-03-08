from .TextFilter import TextFilter

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