from environs import Env
from dataclasses import dataclass


@dataclass
class BaseConfig:
    '''Base config class for a Chat_GPT tool'''

    openai_api_key: str


def load_config(path: str | None = None) -> BaseConfig:
    '''Config loader for a Chat_GPT tool'''

    env = Env()
    env.read_env(path)
    return BaseConfig(
        openai_api_key=env.str('OPENAI_API_KEY')
    )
