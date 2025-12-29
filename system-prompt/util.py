import os
from dotenv import load_dotenv


def load_environ():
    """環境変数ロード

    Returns:
        dict[str, str]: 環境変数dict
    """
    load_dotenv()

    env = {
        "DICTIONARY_FILE": os.environ["DICTIONARY_FILE"],
        "OPENAI_API_KEY": os.environ["OPENAI_API_KEY"],
        "GPT_MODEL": os.environ["GPT_MODEL"],
    }
    return env
