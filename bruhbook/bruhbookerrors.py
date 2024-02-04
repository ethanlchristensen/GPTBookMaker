class BruhBookError(Exception):
    pass


class ApiKeyNotFoundError(BruhBookError):
    def __init__(
        self,
        value,
        message="OpenAI API key not found! Pass this into the `api_key` variable in the BruhBook constructor, or set an `OPENAI_API_KEY` environment variable.",
    ):
        self.value = value
        self.message = message
        super().__init__(self.message)


class InvalidParameterValueError(BruhBookError):
    def __init__(self, value: any, parameter: str, options: list[any] = None):
        self.message = f"Value of '{value}' is not valid for parameter '{parameter}'. Valid options are {options}"
        super().__init__(self.message)


class UnhandledExceptionError(BruhBookError):
    def __init__(
        self,
        value,
        message="",
    ):
        self.value = value
        self.message = message
        super().__init__(self.value)


class MissingParameterError(BruhBookError):
    def __init__(self, value, message="Missing value for parameter `%s`."):
        self.value = value
        self.message = message % value
        super().__init__(self.message)

