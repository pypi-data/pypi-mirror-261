def deep_map(data: dict | list, func_cond, func_map):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (list, dict)):
                null_to_zero(value)
            elif func_cond(value):
                data[key] = func_map(value)
    elif isinstance(data, list):
        for index, value in enumerate(data):
            if isinstance(value, (list, dict)):
                null_to_zero(value)
            elif func_cond(value):
                data[index] = func_map(value)


def null_to_zero(data: dict | list):
    return deep_map(data, lambda value: value is None, lambda _: 0)


def deep_round(data: dict | list, ndigits: int):
    return deep_map(data, lambda value: isinstance(value, float), lambda value: round(value, ndigits))


class EData:
    def __init__(self, data):
        self.data = data

    def null_to_zero(self):
        null_to_zero(self.data)

    def round(self, ndigits: int):
        deep_round(self.data, ndigits)
