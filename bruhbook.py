import re
import os
import docx
import openai
import requests

from docx.shared import Inches
from docx2pdf import convert
from bruhcolor import bruhcolored as bc
from dotenv import load_dotenv


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


class BruhBook:
    def __init__(self, api_key: str | None = None, create_cover_image: bool = False):
        """_summary_

        Args:
            api_key (str | None, optional): _description_. Defaults to None.
            create_cover_image (bool, optional): _description_. Defaults to False.

        Raises:
            ApiKeyNotFoundError: _description_
        """

        if api_key:
            self.__api_key = api_key
        elif ak := os.getenv("OPENAI_API_KEY"):
            self.__api_key = ak
        else:
            raise ApiKeyNotFoundError(None)

        self.__openai_client = openai.OpenAI()
        self.__generation_model = "gpt-3.5-turbo-0125"
        self.__image_model = "dall-e-3"
        self.___create_cover_image = create_cover_image
        self.__story_outline = None
        self.__prompts = {
            "image_prompt_creator_prompt": {"system": "", "user": ""},
            "title_creator_prompt": {"system": "", "user": ""},
            "partial_story_generator": {"system": "", "user": ""},
        }

        self.__home_directory = os.getcwd()

        self.__check_for_folders()

    def __check_for_folders(self):
        """_summary_"""

        stories_path = self.__home_directory + "/stories"
        if not os.path.exists(stories_path):
            os.mkdir(stories_path)

    def set_generation_model(self, model: str):
        self.__generation_model = model

    def __openai_prompter(
        self,
        system_prompt: str,
        user_prompt: str,
        api_type: str = "generate",
        image_path: str | None = None,
        model: str | None = None,
    ):
        """_summary_

        Args:
            system_prompt (str): _description_
            user_prompt (str): _description_
            api_type (str, optional): _description_. Defaults to "generate".
            image_path (str | None, optional): _description_. Defaults to None.

        Raises:
            InvalidOpenAIPrompterType: _description_
        """

        if api_type == "generate":
            try:
                return (
                    self.__openai_client.chat.completions.create(
                        messages=[],
                        temperature=0.5,
                        max_tokens=1500,
                        model=model if model else self.__generation_model,
                    )
                    .choices[0]
                    .message.content
                )
            except Exception as e:
                raise UnhandledExceptionError(str(e))

        elif api_type == "image":
            if image_path:
                pass
            else:
                raise MissingParameterError("image_path")
        else:
            raise InvalidParameterValueError(
                value=api_type, parameter="api_type", options=["generate", "image"]
            )
